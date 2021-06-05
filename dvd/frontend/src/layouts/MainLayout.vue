<template lang="pug">
q-layout(view='hHr LpR ffr')
  q-header.bg-primary.text-white(elevated='', height-hint='98')
    q-toolbar
      q-toolbar-title
        | Herramienta administración de catalogos
      q-btn(v-if='!isAuthenticated' to='/auth/login' label='Identificarse' icon-right='login' dense flat)
      q-btn(v-if='isAuthenticated'  @click='logout' :label="`Cerrar sesión: ${user.username}`" icon-right='logout' dense flat)

  q-page-container
    router-view

</template>

<script>
import { computed, reactive } from 'vue'
import { defineComponent, ref } from 'vue'
import { useStore } from 'vuex'
export default defineComponent({
  name: 'MainLayout',
  components: {
  },
  setup () {

    const store = useStore()
    const isAuthenticated = computed(() => store.state.auth.isAuthenticated)
    const verifyAuth = () => {
      store.dispatch('verifyAuth')
    }
    verifyAuth()
    const logout = () => {
      store.dispatch('logout')
      //layout.drawerIsExpanded = false
    }

    return {

      isAuthenticated,
      user: computed(() => store.state.auth.user),
      logout,
    }
  }
})
</script>
