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
    </div>
  </div>
</template>

<script>

import HousingApi from '@/API/HousingApi';

export default {
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
			await housingApi.login(this.username, this.password)
		} catch (error) {
			console.error(error)
		}
	}
  }
}

</script>
