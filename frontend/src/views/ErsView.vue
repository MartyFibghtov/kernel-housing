<template>
  <div class="container md">
    <div class="row">
      <div class="col">
        <form @submit.prevent="searchForRequests">
          <div class="form-group d-flex">
            <input class="form-control flex-grow-1" type="text" placeholder="Search for entrance requests..." v-model="searchRequest" v-on:input="searchForRequests">
            <button class="btn btn-primary ml-2" type="submit">Search</button>
          </div>
        </form>
        <table class=" table">
          <thead>
            <tr>
              <th>Car</th>
              <th>Is Paid</th>
              <th>Note</th>
              <th>Request Account</th>
              <th>Date Created</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="request in shownRequest" :key="request.id">
              <td>{{ request.car.car_number }}</td>
              <td>{{ request.is_paid }}</td>
              <td>{{ request.note }}</td>
              <td>{{ request.request_account.address_name }}</td>
              <td>{{ formatDate(request.date_created) }}</td>
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
      shownRequest: [],
      searchRequest: "",
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
        this.shownRequest = response;
        console.log(this.response);
      } catch (error) {
        console.error(error);
      }
    },
    searchForRequests() {
      try {
        var tempArr = [];
        const searchLower = this.searchRequest.toLowerCase();

        // for (var i = 0; i < this.requests.length; i++)
        // {
        //   if 
        // }
        this.shownRequest = this.requests.filter((x) => x.car.car_number.toLowerCase().indexOf(searchLower) > -1)
      } catch (error) {
        console.error(error);
      }
    },
    formatDate(dateStr) {
      const date = new Date(dateStr);

      const formatter = new Intl.DateTimeFormat('ru', {
        hour: '2-digit',
        minute: '2-digit',
        day: '2-digit',
        month: '2-digit',
        hour12: false,
      });

      return formatter.format(date);
    }
  },
};
</script>


