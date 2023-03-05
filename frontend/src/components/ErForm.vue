<template>
  <div class="container-sm">
    <form class="p-3" @submit.prevent="handleSubmit">
      <div class="row mb-3">
        <label for="account-select" class="col-sm-3 col-form-label"
          >Account:</label
        >
        <div class="col-sm-9">
          <select
            id="account-select"
            v-model="selectedAccount"
            class="form-select"
          >
            <option
              v-for="account in accounts"
              :key="account.id"
              :value="account.id"
            >
              {{ account.address_name }}
            </option>
          </select>
        </div>
      </div>

      <div class="row mb-3">
        <label for="car-select" class="col-sm-3 col-form-label">Car:</label>
        <div class="col-sm-9">
          <select id="car-select" v-model="selectedCar" class="form-select">
            <option v-for="car in cars" :key="car.id" :value="car.id">
              {{ car.car_number }}
            </option>
          </select>
        </div>
      </div>

      <div class="row mb-3">
        <label for="is-paid" class="col-sm-3 col-form-label">Is Paid:</label>
        <div class="col-sm-9">
          <div class="form-check form-switch">
            <input
              type="checkbox"
              id="is-paid"
              v-model="isPaid"
              class="form-check-input"
            />
            <label for="is-paid" class="form-check-label ms-2">{{
              isPaid ? "Yes" : "No"
            }}</label>
          </div>
        </div>
      </div>

      <div class="row mb-3">
        <label for="note" class="col-sm-3 col-form-label">Note:</label>
        <div class="col-sm-9">
          <textarea
            id="note"
            v-model="note"
            class="form-control"
            rows="3"
          ></textarea>
        </div>
      </div>

      <div class="row justify-content-center">
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </form>
  </div>
</template>
  
  
  <script>
import HousingApi from "@/API/HousingApi";
var housingApi = new HousingApi();

export default {
  name: "ErForm",
  data() {
    return {
      accounts: null,
      selectedAccount: null,
      cars: null,
      selectedCar: null,
      isPaid: false,
      note: "",
    };
  },
  mounted() {
    this.loadCarsAccounts();
  },
  methods: {
	async loadCarsAccounts() {
		this.cars = await housingApi.getAllCars();
		this.accounts = await housingApi.getAllPersonalAccounts();
	},
    async handleSubmit() {
      if (this.selectedAccount && this.selectedCar) {
        let resp = await housingApi.createEntranceRequest(
          this.selectedAccount,
          this.selectedCar,
		  true,
          this.isPaid,
          this.note
        );
		this.selectedAccount = null;
		this.selectedCar = null;
		this.isPaid = null;
		this.note = ""

      } else {
        alert("Please select an account and a car");
      }
    },
  },
};
</script>
  