<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Username</label>
            <input
              type="text"
              class="form-control"
              id="username"
              v-model="username"
            />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input
              type="password"
              class="form-control"
              id="password"
              v-model="password"
            />
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
      <log-out-button></log-out-button>
    </div>
  </div>
</template>

<script>

import HousingApi from '@/API/HousingApi';
import LogOutButton from '../components/LogOutButton.vue';

export default {
  components: { LogOutButton },
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
	async submitForm() {
		var housingApi = new HousingApi()
		try {
			await housingApi.login(this.username, this.password);
      this.username = '';
      this.password = '';
		} catch (error) {
			this.$toast.error(error.message)
		}
	}
  }
}

</script>
