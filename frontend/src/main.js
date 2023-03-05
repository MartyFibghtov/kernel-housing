import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// import './registerServiceWorker'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

createApp(App).use(router).mount("#app");
