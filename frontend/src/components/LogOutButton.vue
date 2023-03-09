<template>
	<div>
	  <button class="btn btn-primary" @click="logout">Logout</button>
	</div>
</template>
  
  <script>
  import HousingApi from "@/API/HousingApi";
  
  export default {
	name: "logOutButton",
	data() {
	  return {
		api: new HousingApi()
	  }
	},
	mounted() {
	  // Check if user is authenticated
	},
	methods: {
	  async logout() {
		try {
		  await this.api.logout();
		  // Do something after logout
		} catch (error) {
			this.$toast.error(error.message);
		}
	  }
	}
  }
  </script>
  