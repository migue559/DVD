<template lang="pug">
q-page.window-height.window-width.row.justify-center.items-center(style='background: linear-gradient(#8274C5, #5A4A9F);')
  q-card.shadow-24(square='', style='width:300px;height:485px;')
    q-card-section
      q-form.q-px-sm.q-pt-xl
        q-input(square='', clearable='', v-model='user.username', label='User')
          template(v-slot:prepend='')
            q-icon(name='ti-user')
        q-input(square='', clearable='', v-model='user.password', type='password', label='Password')
          template(v-slot:prepend='')
            q-icon(name='ti-lock')
    q-card-actions.q-px-lg
      q-btn.fit.text-white( size='md', color='info', label='Entrar' @click='login(user)')
    q-card-section.text-center.q-pa-sm
      p.text-grey-6 Forgot your password?

</template>

<script>
import { defineComponent, reactive } from 'vue';
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
//import { apollo } from '@boot/apollo'

export default defineComponent({
  name: 'PageLogin',

  setup(){
    const store = useStore()
    const router = useRouter()
    const user = reactive({
      username:"admin",
      password :"admin",
    })
    const login = (user) => {

      if(user){
        console.log(user)
        store.dispatch('login', user)
        .then((data) => {
          if (data.token) router.push({ name: 'Index' })
        })
        //router.push({ name: 'Home' })
      }else{
        console.log(`usuario no permitido ${user.name}`)

      }

    }
    return {
      user,
      login
    }
  }
})
</script>
