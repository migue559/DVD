<template lang="pug">
q-page.flex.flex-center
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
    result:''
  })
  const makeSearch = () => {
    apollo
      .query({
        query: cataloguesHiveQuery()
        //query: cataloguesHiveQuery(id.value, 'query')
      }).then(({ data }) => {
        console.log(data)
        search.results = data.hiveCatalogueQuery.edges.map((edge) => {
          return edge.node
        })
        console.log("makequery", search.results)
      }).catch((error) => {
        console.error('HiveCatalogue, makeQuery:', error)
      })
  }
  makeSearch()
  return {
     search, flat
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
