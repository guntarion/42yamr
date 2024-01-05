import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/question/:slug",
    name: "question",
    // route level code-splitting
    // this generates a separate chunk (question-time.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "question-time" */ "../views/Question.vue"),
    props: true,
  },
  {
    path: "/ask/:slug?", // with ? slug is optional
    name: "question-editor",
    component: () =>
      import(
        /* webpackChunkName: "question-editor" */ "../views/QuestionEditor.vue"
      ),
  },
  {
    path: "/answer/:uuid",
    name: "answer-editor",
    component: () =>
      import(
        /* webpackChunkName: "answer-editor" */ "../views/AnswerEditor.vue"
      ),
    props: true,
  },
  {
    path: "/:catchAll(.*)",
    name: "page-not-found",
    component: () =>
      import(/* webpackChunkName: "not-found" */ "../views/NotFound.vue"),
  },
];

const router = createRouter({
  // history: createWebHistory(process.env.BASE_URL),
  history: createWebHistory("/"),
  routes
})

export default router
