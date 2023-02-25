import axios from 'axios';

class HousingApi {
    constructor() {
        this.apiBaseUrl = "http://127.0.0.1:8000/";
        this.authToken = "3e5fa5ad3a05dde03edb3958c729308f8beaba90";
    }

    getAuthorizationHeader() {
        const headers = { 'Authorization': `Token ${this.authToken}` };
        return headers;
    }

    async getToken(username, password) {
        const url = `${this.apiBaseUrl}/api/token-auth/`;
        const headers = { 'Content-Type': 'application/json' };
        const body = JSON.stringify({ username, password });
        const response = await fetch(url, { method: 'POST', headers, body });
        const data = await response.json();
        return data.token;
    }

    async getAllCars() {
        const url = `${this.apiBaseUrl}/api/cars/get-all/`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        return data.result;
    }

    async getCarById(carId) {
        const url = `${this.apiBaseUrl}/api/cars/get-by-id/?car_id=${carId}`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        return data.result;
    }

    async createCar(carNumber, carType, carMark, owner = null) {
        const url = `${this.apiBaseUrl}/api/cars/create/`;
        const headers = {
            'Content-Type': 'application/json',
            ...this.getAuthorizationHeader()
        };
        const body = JSON.stringify({ car_number: carNumber, car_type: carType, car_mark: carMark, owner: owner });
        const esponse = await fetch(url, { method: 'POST', headers, body });
        const data = await response.json();
        return data.result;
    }

    async getAllCarMarks() {
        const url = `${this.apiBaseUrl}/api/cars/marks/get-all/`;
        console.log(url)
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        return data.result;
    }

    async getAllCarTypes() {
        const url = `${this.apiBaseUrl}/api/cars/types/get-all/`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        return data.result;
    }


    async getAllEntranceRequests(periodStart = null, periodEnd = null) {
        const url = new URL(`${this.apiBaseUrl}/api/entrance-request/get-all/`);
        if (periodStart) {
            url.searchParams.set('period_start', periodStart);
        }
        if (periodEnd) {
            url.searchParams.set('period_end', periodEnd);
        }
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        return data.result;
    }

    async getEntranceRequestById(id) {
        const url = `${this.apiBaseUrl}/api/entrance-request/get-by-id?id=${id}`;
        const headers = this.getAuthorizationHeader();
        const response = await axios.get(url, { headers });
        return response.data;
    }

    async createEntranceRequest(request_account, car, is_car, is_paid, note) {
        const url = `${this.apiBaseUrl}/api/entrance-request/create`;
        const headers = this.getAuthorizationHeader();
        const data = { request_account, car, is_car, is_paid, note };
        const response = await axios.post(url, data, { headers });
        return response.data;
    }

    async deleteEntranceRequestById(id) {
        const url = `${this.apiBaseUrl}/api/entrance-request/delete-by-id?id=${id}`;
        const headers = this.getAuthorizationHeader();
        const response = await axios.delete(url, { headers });
        return response.data;
    }
}

export default HousingApi;