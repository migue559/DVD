<template lang="pug">
q-page.flex.flex-center
  | index
  //HiveCatalogue
</template>

<script>
import { defineComponent } from 'vue';
import HiveCatalogue from '../components/hac/catalogues'

export default defineComponent({
  name: 'PageIndex',
  components:{
    HiveCatalogue
  },
})
</script>
