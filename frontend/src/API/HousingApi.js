import axios from 'axios';
import Cookies from 'js-cookie'

class HousingApi {
    constructor() {
        this.token = Cookies.get('token')
        this.apiBaseUrl = "http://127.0.0.1:8000/";
        this.authToken = "";
    }

    getResponseData(data) {
        if (!data.success)
        {
            throw new Error("Error! " + data.message);
        }
        return data.result;
    }

    getAuthorizationHeader() {
        const headers = { 'Authorization': `Token ${this.token}` };
        return headers;
    }

    async login(username, password) {
        const url = `${this.apiBaseUrl}/api/token-auth/`;
        const headers = { 'Content-Type': 'application/json' };
        const body = JSON.stringify({ username, password });
        const response = await fetch(url, { method: 'POST', headers, body });
        const data = await response.json();

        // Set token to cookie
        Cookies.set('token', data.token)
        return data.token;
    }

    async logout(){
        Cookies.remove('token');
        this.token = null;
    }

    async getAllCars() {
        const url = `${this.apiBaseUrl}/api/cars/get-all/`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();

        return this.getResponseData(data);
    }

    async getCarById(carId) {
        const url = `${this.apiBaseUrl}/api/cars/get-by-id/?car_id=${carId}`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();

        return this.getResponseData(data);
    }

    async createCar(carNumber, carType, carMark, owner = null) {
        const url = `${this.apiBaseUrl}/api/cars/create/`;
        const headers = {
            'Content-Type': 'application/json',
            ...this.getAuthorizationHeader()
        };
        const body = JSON.stringify({ car_number: carNumber, car_type: carType, car_mark: carMark, owner: owner });
        const response = await fetch(url, { method: 'POST', headers, body });
        const data = await response.json();

        return this.getResponseData(data);
    }

    async getAllCarMarks() {
        const url = `${this.apiBaseUrl}/api/cars/marks/get-all/`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        
        return this.getResponseData(data);
    }

    async getAllCarTypes() {
        const url = `${this.apiBaseUrl}/api/cars/types/get-all/`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        
        return this.getResponseData(data);
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
        
        return this.getResponseData(data);
    }

    async getAllEntranceRequestsWithSubdata(periodStart = null, periodEnd = null) {
        var ers = await this.getAllEntranceRequests(periodStart = null, periodEnd = null);
        var personalAccounts = await this.getAllPersonalAccounts();
        var cars = await this.getAllCars();

        ers.forEach(er => {
            er.car = cars.find(element => element.id === er.car)
            er.request_account = personalAccounts.find(element => element.id === er.request_account)
        });

        return ers;
    }

    async getEntranceRequestById(id) {
        const url = `${this.apiBaseUrl}/api/entrance-request/get-by-id?id=${id}`;
        const headers = this.getAuthorizationHeader();
        const response = await axios.get(url, { headers });
        
        return this.getResponseData(data);
    }

    async createEntranceRequest(request_account, car, is_car, is_paid, note) {
        const url = `${this.apiBaseUrl}/api/entrance-request/create/`;
        const headers = this.getAuthorizationHeader();
        const data = { request_account, car, is_car, is_paid, note };
        const response = await axios.post(url, data, { headers });
        
        return this.getResponseData(data);
    }

    async deleteEntranceRequestById(id) {
        const url = `${this.apiBaseUrl}/api/entrance-request/delete-by-id?id=${id}`;
        const headers = this.getAuthorizationHeader();
        const response = await axios.delete(url, { headers });
        
        return this.getResponseData(data);
    }

    async getAllPersonalAccounts() {
        const url = `${this.apiBaseUrl}/api/address/personal-account/get-all/`;
        const headers = this.getAuthorizationHeader();
        const response = await fetch(url, { headers });
        const data = await response.json();
        
        return this.getResponseData(data);
    }

}

export default HousingApi;
