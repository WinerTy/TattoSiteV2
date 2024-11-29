import { createRouter, createWebHistory } from 'vue-router'
import { RouteNames, RoutePath } from '@/types/router.type'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import MasterCatalog from '../views/MasterCatalog.vue'
import AboutSalon from '@/views/AboutSalon.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: RoutePath.Home,
      name: RouteNames.Home,
      component: HomeView,
    },
    {
      path: RoutePath.About,
      name: RouteNames.About,
      component: AboutView,
    },
    {
      path: RoutePath.Masters,
      name: RouteNames.Masters,
      component: MasterCatalog,
    },
    {
      path: RoutePath.AboutSalon,
      name: RouteNames.AboutSalon,
      component: AboutSalon,
    },
  ],
})

export default router
