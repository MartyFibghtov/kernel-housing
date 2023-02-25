<template>
  <h1>CAr</h1>
  <button @click="test">BUTTON</button>
</template>

<script>
import HousingApi from "@/API/HousingApi";

const apiBaseUrl = "http://127.0.0.1:8000/";

export default {
  name: "ErsView",
  components: {},
  methods: {
    async test() {
      console.log("called")
      const gateRequestManager = new HousingApi();
      // Get all cars
      const cars = await gateRequestManager.getAllCars();
      console.log(cars);
    },
  },
};
</script>

