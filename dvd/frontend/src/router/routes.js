
const routes = [
  {
    path: '/auth/login', component: () => import('layouts/AuthLayout.vue'),
    children: [
      { path: '/auth/login', name:'Login', component: () => import('@pages/Login.vue') },
    ]
  },
  {
    path: '/',  component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '',name:'Index', component: () => import('@pages/Index.vue') },
      { path: '/Table',name:'Table', component: () => import('@pages/Table.vue') },

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
