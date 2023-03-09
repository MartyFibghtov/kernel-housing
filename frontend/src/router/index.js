import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/entrance-request/create",
    component: () => import("../views/CreateErView.vue"),
  },
  {
    path: "/entrance-request/all",
    component: () => import("../views/ErsView.vue"),
  },
  {
    path: "/login",
    component: () => import("../views/LoginView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
