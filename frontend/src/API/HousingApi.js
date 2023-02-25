import axios from 'axios';

class HousingApi {
    constructor(apiBaseUrl, authToken) {
        this.apiBaseUrl = apiBaseUrl;
        this.authToken = authToken;
    }

    getAuthorizationHeader() {
        headers = { 'Authorization': `Token ${this.authToken}` };
        return headers;
    }

    async getToken(username, password) {
        url = `${this.apiBaseUrl}/api/token-auth/`;
        headers = { 'Content-Type': 'application/json' };
        body = JSON.stringify({ username, password });
        response = await fetch(url, { method: 'POST', headers, body });
        data = await response.json();
        return data.token;
    }

    async getAllCars() {
        url = `${this.apiBaseUrl}/api/cars/get-all/`;
        headers = this.getAuthorizationHeader();
        response = await fetch(url, { headers });
        data = await response.json();
        return data.result;
    }

    async getCarById(carId) {
        url = `${this.apiBaseUrl}/api/cars/get-by-id/?car_id=${carId}`;
        headers = this.getAuthorizationHeader();
        response = await fetch(url, { headers });
        data = await response.json();
        return data.result;
    }

    async createCar(carNumber, carType, carMark, owner = null) {
        url = `${this.apiBaseUrl}/api/cars/create/`;
        headers = {
            'Content-Type': 'application/json',
            ...this.getAuthorizationHeader()
        };
        body = JSON.stringify({ car_number: carNumber, car_type: carType, car_mark: carMark, owner: owner });
        response = await fetch(url, { method: 'POST', headers, body });
        data = await response.json();
        return data.result;
    }

    async getAllCarMarks() {
        url = `${this.apiBaseUrl}/api/cars/marks/get-all/`;
        headers = this.getAuthorizationHeader();
        response = await fetch(url, { headers });
        data = await response.json();
        return data.result;
    }

    async getAllCarTypes() {
        url = `${this.apiBaseUrl}/api/cars/types/get-all/`;
        headers = this.getAuthorizationHeader();
        response = await fetch(url, { headers });
        data = await response.json();
        return data.result;
    }


    async getAllEntranceRequests(periodStart = null, periodEnd = null) {
        url = new URL(`${this.apiBaseUrl}/api/entrance-request/get-all/`);
        if (periodStart) {
            url.searchParams.set('period_start', periodStart);
        }
        if (periodEnd) {
            url.searchParams.set('period_end', periodEnd);
        }
        headers = this.getAuthorizationHeader();
        response = await fetch(url, { headers });
        data = await response.json();
        return data.result;
    }

    async getEntranceRequestById(id) {
        url = `${this.apiBaseUrl}/api/entrance-request/get-by-id?id=${id}`;
        headers = this.getAuthorizationHeader();
        response = await axios.get(url, { headers });
        return response.data;
    }

    async createEntranceRequest(request_account, car, is_car, is_paid, note) {
        url = `${this.apiBaseUrl}/api/entrance-request/create`;
        headers = this.getAuthorizationHeader();
        data = { request_account, car, is_car, is_paid, note };
        response = await axios.post(url, data, { headers });
        return response.data;
    }

    async deleteEntranceRequestById(id) {
        url = `${this.apiBaseUrl}/api/entrance-request/delete-by-id?id=${id}`;
        headers = this.getAuthorizationHeader();
        response = await axios.delete(url, { headers });
        return response.data;
    }
}

export default SynonymsAPI;
