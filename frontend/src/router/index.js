import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: 'home',
    name: 'Main',
    component: () => import('../views/MainHomeView.vue'),
    children: [
      {
        path: 'home',
        component: () => import('../views/HomeView.vue'),
        children: [
          {
            path: 'login',
            component: () => import('../components/Login.vue'),
          },
          {
            path: 'register',
            component: () => import('../components/Register.vue'),
          },
          {
            path: 'reset',
            component: () => import('../components/forgot_password.vue'),
          }
        ]
      },
      {
        path: 'faqs',
        component: () => import('../views/FaqView.vue'),
      }
    ]
  },
  {
    path: '/dashboard',
    redirect: '/dashboard/summary',
    name: 'Dashboard',
    component: () => import('../views/MainDashboardView.vue'),
    children: [
      {
        path: 'summary',
        component: () => import('../views/Summary.vue'),
      },
      {
        path: 'trackers',
        component: () => import('../views/Trackers.vue'),
      },
      {
        path: 'trackersLogs',
        component: () => import('../views/TrackersLogs.vue'),
      },
      {
        path: 'updateDetails',
        component: () => import('../views/UpdateDetails.vue')

      }
    ],
  },
  {
    path: '/logout',
    name: "Logout",
    component: () => import('../components/Logout.vue'),
  },
  {
    path: '*',
    component: () => import("../views/NotFound.vue"),
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
