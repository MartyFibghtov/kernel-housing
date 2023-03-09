import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";


// import toast
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

// import './registerServiceWorker'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

const app = createApp(App);

// Add toast to Vue prototype
app.config.globalProperties.$toast = toast;

app.use(router).mount("#app");
