<template lang="pug">
q-layout(view='hHr LpR ffr')
  q-header.bg-primary.text-white(elevated='', height-hint='98')
    q-toolbar
      q-toolbar-title
        | Herramienta administración de catalogos
      q-btn(v-if='!login', dense='', flat='', round='', icon='menu', @click='right = !right')
      q-btn(v-else='login', dense='', flat='', round='', icon='ti-user', @click='right = !right')
        q-drawer(show-if-above='', v-model='right', side='right', bordered='')
          q.h2 content

  q-page-container
    router-view

</template>

<script>
import { defineComponent, ref } from 'vue'
export default defineComponent({
  name: 'MainLayout',
  components: {
  },
  setup () {
    const right = ref(false);
    const login = ref(false);
    return {
      right,
      login,
    }
  }
})
</script>
