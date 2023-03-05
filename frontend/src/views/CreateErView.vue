<template>
  <div class="container">
    <car-form></car-form>
    <er-form></er-form>
  </div>
</template>

<script>
import CarForm from "../components/CarForm.vue";
import ErForm from "../components/ErForm.vue";

export default {
  name: "CreateErView",
  components: { ErForm, CarForm },
};
</script>
