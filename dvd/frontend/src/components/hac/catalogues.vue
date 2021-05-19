<template lang="pug">
q-card.my-card.bg-blue-grey-2(flat='', bordered='')
  q-toolbar.bg-blue-grey-6.text-white
    .text-h6 {{ hiveCatalogue.hiveCatalogueID.name }}
    q-space
    q-btn(flat='' round='' dense='' size='sm' :icon='hiveCatalogue.hiveCatalogueID.isPublic ? "public" : "lock"')
  q-card-section
    .row.items-center.no-wrap
      .col
        .text-subtitle1 {{ hiveCatalogue.hiveCatalogueID.description }}
  q-toolbar.q-my-md.shadow-2
    q-space
    q-separator(dark='' vertical='')
    q-btn(stretch='' flat='' :label='hiveCatalogue.hiveCatalogueID.downloads' size='sm' icon='file_download')
    q-separator(dark='' vertical='')
    q-btn(stretch='' flat='' :label='hiveCatalogue.hiveCatalogueID.views' size='sm' icon='preview')


</template>

<script>

import { defineComponent, toRef,reactive} from 'vue'
import { singleHiveTableQuery } from '@endpoints/hac.endpoints'
import { apollo } from '@boot/apollo';

function hiveCatalogues (id) {
  const hiveCatalogue = reactive({
    hiveCatalogueID: {}
  })
  const makeQuery = () => {
    apollo
      .query({
        query: singleHiveTableQuery(id.value)
      }).then(({ data }) => {
        hiveCatalogue.hiveCatalogueID = data.hiveCatalogueID
      }).catch((error) => {
        console.error('HiveCatalogue, makeQuery:', error)
      })
  }
  const makeSubscribe = () => {
    apollo.subscribe({
      query: singleHiveTableQuery(id.value)
    }).subscribe({
      next ({ data }) {
        hiveCatalogue.hiveCatalogueID = data.hiveCatalogueSubscription
      },
      error (error) {
        console.error('HiveCatalogue, makeSubscribe:', error)
      }
    })
  }
  makeQuery()
  //makeSubscribe()
  return { hiveCatalogue, makeQuery }
}

export default defineComponent({
  name: 'HiveCatalogue',
  props:{
    id:{
      type:String,
      required:true
    },
    name:{
      type:String,
      required:true
    },
    views:{
      type:Number,
      required:true
    },
    flat:{
      type:Boolean,
      required:false,
      default:false
    }
  },
  setup(props) {

    return {
      ...hiveCatalogues(toRef(props,'id'))

    }


  }



})


</script>
