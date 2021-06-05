<template lang="pug">
q-layout(view='hHh lpR fFf')
  q-page-container
    router-view
</template>

<style lang="sass" scoped>
.bg-auth

  background-size: cover
  background-repeat: no-repeat
</style>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'AuthLayout'
})
</script>
