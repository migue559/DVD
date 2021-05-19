<template lang="pug">
q-page.q-pa-md
  .row.q-mb-lg.q-col-gutter-sm
    .col-8
      q-card(style="max-width:550px")
        q-card-section
          .text-weight-bold.text-secondary BUSQUEDA DE CATÁLOGOS
          //q-input( v-model='search.key' @update:model-value='makeSearch' debounce='500' autofocus counter='' maxlength='150')
          //@update realiza evento makesearch 500 milisegundos despues de haber escrito algo en el form text
          q-input( v-model="search.key" ,@keyup.enter="makeSearch", maxlength='110')
            q-btn( icon="search", @click="makeSearch")
          // esta una version diferente de hacer la busqueda con botton y con enter en el input text


    .col-4
      q-card(style="max-width:400px")
          q-card-section
            .text-secondary Obtiene una lista de los catalogos a los cuales acceso (solo publicos **)

  .row.q-col-gutter-md
    .col-4(v-for='result in search.results')
      HiveCatalogue.cursor-pointer(
        v-bind:="result"
        v-bind:flat="flat"
      )
</template>

<script>
import HiveCatalogue from '../components/hac/catalogues'
import { defineComponent, toRef, reactive } from 'vue';
import { apollo } from '@boot/apollo';
import { cataloguesHiveQuery} from '@endpoints/hac.endpoints'

//function hiveCatalogues (id) {
function hiveCatalogues () {
  const flat = true
  const search = reactive({
    results:[],
    result:'',
    key:''
  })
  const makeSearch = () => {
    console.log("id",search.key)
    apollo
      .query({
        query: cataloguesHiveQuery(search.key)
        //query: cataloguesHiveQuery(id.value, 'query')
      }).then(({ data }) => {
        search.results = data.hiveCatalogueQuery.edges.map((edge) => {
          return edge.node
        })
      }).catch((error) => {
        console.error('cataloguesHiveQuery error, makeQuery:', error)
      })
  }
  makeSearch()
  return {
     search, flat, makeSearch
  }
}
export default defineComponent({
  name: 'PageIndex',
  components:{
    HiveCatalogue
  },

  setup () {
    return {
      ...hiveCatalogues()
    }
  }
})
</script>
