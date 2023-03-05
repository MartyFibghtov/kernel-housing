<template>
  <div class="container-sm">
    <form class="p-3" @submit.prevent="handleSubmit">
      <!-- Number -->
	  <div class="row mb-3">
		
		<label for="account-select" class="col-sm-3 col-form-label"
          >Number:</label
        >
		<div class="col-sm-9">
	  		<input v-model="number" class="form-control">
		</div>
	
	
	</div>
      <!-- Account -->
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

      <!-- Car type -->
      <div class="row mb-3">
        <label for="type-select" class="col-sm-3 col-form-label"
          >Car Type:</label
        >
        <div class="col-sm-9">
          <select id="type-select" v-model="selectedType" class="form-select">
            <option
              v-for="carType in carTypes"
              :key="carType.id"
              :value="carType.name"
            >
              {{ carType.name }}
            </option>
          </select>
        </div>
      </div>

      <!-- Car mark -->
      <div class="row mb-3">
        <label for="mark-select" class="col-sm-3 col-form-label"
          >Car Mark:</label
        >
        <div class="col-sm-9">
          <select id="mark-select" v-model="selectedMark" class="form-select">
            <option
              v-for="carMark in carMarks"
              :key="carMark.id"
              :value="carMark.name"
            >
              {{ carMark.name }}
            </option>
          </select>
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
  name: "CarForm",
  data() {
    return {
      number: "",

      carMarks: [],
      selectedMark: null,

      carTypes: [],
      selectedType: null,

      accounts: [],
      selectedAccount: null,
    };
  },
  mounted() {
    this.loadMarksTypesAccounts();
  },
  methods: {
    async loadMarksTypesAccounts() {
      this.carMarks = await housingApi.getAllCarMarks();
      this.carTypes = await housingApi.getAllCarTypes();
      this.accounts = await housingApi.getAllPersonalAccounts();
    },
    async handleSubmit() {
      if (this.number) {
        let resp = await housingApi.createCar(
          this.number,
          this.selectedType,
          this.selectedMark,
          this.accounts[this.selectedAccount - 1].address_name
        );

        this.selectedAccount = null;
        this.selectedCar = null;
        this.isPaid = null;
        this.note = "";
      } else {
        alert("Please select an account and a car");
      }
    },
  },
};
</script>
	