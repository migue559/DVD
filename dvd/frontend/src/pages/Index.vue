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
            q-btn( icon="ti-search", @click="makeSearch")
          // esta una version diferente de hacer la busqueda con botton y con enter en el input text
          // v model guarda el valor y lo asigna akey y el evento se ejecuta de dos maneras se manda a ejecutar la funcion makesearch por pulsar el boton y hacer clik enter


    .col-4
      q-card(style="max-width:400px")
          q-card-section
            .text-secondary Obtiene una lista de los catalogos a los cuales acceso (solo publicos **)

  .row.q-col-gutter-md
    .col-4(v-for='result in search.results')
      HiveCatalogue.cursor-pointer(
        v-bind:="result"
        v-bind:flat="flat"
        @click="openTable(result.id)"
      )
</template>

<script>
import HiveCatalogue from '../components/hac/catalogues'
import { defineComponent, toRef, reactive } from 'vue';
import { apollo } from '@boot/apollo';
import { useRouter } from 'vue-router'
import { cataloguesHiveQuery} from '@endpoints/hac.endpoints'

//function hiveCatalogues (id) {
function hiveCatalogues () {
  const router = useRouter()
  const flat = true
  const search = reactive({
    results:[],
    result:'',
    key:''
  })
  const makeSearch = () => {
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
  const openTable = (id) => {
    console.log(`estoy entrando a una nueva pagina, ${id}`)
    router.push({ name: 'Table' , params: { id }})
  }

  makeSearch()

  return {
     search, flat, makeSearch, openTable
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
