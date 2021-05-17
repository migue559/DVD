<template lang="pug">
q-card
  q-toolbar.bg-primary.text-white
    .text-weight-bold {{hiveCatalogue.hiveCatalogueID.name}}
    q-space
    q-btn(flat='' round='' dense='' size='sm' :icon='hiveCatalogue.hiveCatalogueID.isPublic ? "public" : "lock"')
  q-card-section
    .text-caption {{hiveCatalogue.hiveCatalogueID.description}}
  q-toolbar.q-my-md.shadow-2
    q-space
    q-separator(dark='' vertical='')
    q-btn(stretch='' flat='' :label='hiveCatalogue.hiveCatalogueID.downloads' size='sm' icon='file_download')
    q-separator(dark='' vertical='')
    q-btn(stretch='' flat='' :label='hiveCatalogue.hiveCatalogueID.views' size='sm' icon='preview')
</template>

<script>

import { defineComponent, toRef, reactive } from 'vue';
import { apollo } from '@boot/apollo';
import gql from 'graphql-tag'

console.log("sss")
function hiveCatalogues (id) {
  const makeQuery = () => {
    apollo
      .query({
        query: hiveCatalogueType(id.value, 'query')
      }).then(({ data }) => {
        console.log(data)
        hiveCatalogue.hiveCatalogueID = data.hiveCatalogueID
      }).catch((error) => {
        console.error('HiveCatalogue, makeQuery:', error)
      })
  }


}

export default defineComponent({
  name: 'HiveCatalogue',
  props: {
    id: {
      type: String,
      required: true
    },
    flat: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  setup (props) {
    return {
      ...hiveCatalogues(toRef(props, 'id'))
    }
  }
})


</script>
