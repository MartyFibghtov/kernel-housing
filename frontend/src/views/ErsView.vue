<!-- <form @submit.prevent="submitForm">
  <div class="form-group">
    <label for="periodStart">Period Start</label>
    <input
      type="date"
      class="form-control"
      id="periodStart"
      v-model="periodStart"
    />
  </div>
  <div class="form-group">
    <label for="periodEnd">Period End</label>
    <input
      type="date"
      class="form-control"
      id="periodEnd"
      v-model="periodEnd"
    />
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form> -->


<template>
  <div class="container md">
    <div class="row">
      <div class="col">
        <h1>Entrance Requests</h1>
        <table class=" table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Date Created</th>
              <th>Is Car</th>
              <th>Is Paid</th>
              <th>Note</th>
              <th>Request Account</th>
              <th>Car</th>
              <th>Human</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="request in requests" :key="request.id">
              <td>{{ request.id }}</td>
              <td>{{ request.date_created }}</td>
              <td>{{ request.is_car }}</td>
              <td>{{ request.is_paid }}</td>
              <td>{{ request.note }}</td>
              <td>{{ request.request_account.address_name }}</td>
              <td>{{ request.car.car_number }}</td>
              <td>{{ request.human }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<script>
import HousingApi from "@/API/HousingApi";

export default {
  data() {
    return {
      periodStart: null,
      periodEnd: null,
      requests: [],
    };
  },
  mounted() {
    this.loadRequests();
  },
  methods: {
    async loadRequests() {
      console.log("called");
      try {
        var housingApi = new HousingApi();
        const response = await housingApi.getAllEntranceRequestsWithSubdata();
        this.requests = response;
        console.log(this.response);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>


