import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect : 'home',
    name: 'Main',
    component: () => import( '../views/MainView.vue'),
    children : [
      {
        path: 'home',
        component: () => import( '../views/HomeView.vue'),
        children : [
          {
            path: 'login',
            component: () => import( '../components/Login.vue'),
          },
          {
            path: 'register',
            component: () => import( '../components/Register.vue'),
          }
        ]
      },
      {
        path: 'faqs',
        component: () => import( '../views/FaqView.vue'),
      },
      {
        path: 'acknowledgements',
        component: () => import( '../views/AcknowledgementsView.vue'),
      }
    ]
  },
  {
    path: '/dashboard',
    redirect : '/dashboard/summary',
    name: 'Dashboard',
    component : () => import('../views/DashboardView.vue'),
    children : [
      {
        path : 'summary',
        component: () => import( '../components/Summary.vue'),
      },
      {
        path : 'trackers',
        component: () => import( '../components/Trackers.vue'),
      },
      {
        path : 'trackersLogs',
        component: () => import( '../components/TrackersLogs.vue'),
      },
    ],
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
