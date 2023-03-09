# kernel-housing
Django + Vue app for managing gate requests in villages.


API Documentation

[Tokens](#tokens) </br>
[Cars](#cars) </br>
[EntranceRequest](#entrance-request) </br>
[Address](#address) </br>


# Headers
Authorization: Token {auth token}

# Tokens

## Get Token

<details>
 <summary><code>POST</code> <code><b>/api/token-auth/</b></code> <code>(returns users token)</code></summary>

##### Parameters

| name       | type      | data type | description               |
|------------|-----------|-----------|---------------------------|
| `username` | required  | string    | Username that needs token |
| `password` | required  | string    | Users password            |


##### Response
| name      | data type | description                                                                             |
|-----------|-----------|-----------------------------------------------------------------------------------------|
| `token`   | string    | New given token                                                                         |

</details>

--- 

# Cars

<details>
 <summary><code>GET</code> <code><b>/api/cars/get-all/</b></code> <code>(returns all cars)</code></summary>

Permissions: Any authorised user </br>
Statuses:
200
##### Parameters

| name    | type     | data type | description           |
|---------|----------|-----------|-----------------------|

##### Response
| name      | data type    | description                                                                             |
|-----------|--------------|-----------------------------------------------------------------------------------------|
| `result`  | List[string] | A list of existing cars for the given word.                                             |

</details>

<details>
 <summary><code>GET</code> <code><b>/api/cars/get-by-id/</b></code> <code>(returns information about requested car)</code></summary>

Permissions: Any authorised user </br>
Statuses:
200, 404

##### Parameters

| name     | type     | data type | description                      |
|----------|----------|-----------|----------------------------------|
| `car_id` | required | int       | Car id that needs to be returned |

##### Response
| name      | data type    | description                                                                             |
|-----------|--------------|-----------------------------------------------------------------------------------------|
| `result`  | List[string] | A list of existing cars for the given word.                                             |
</details>

<details>
 <summary><code>POST</code> <code><b>/api/cars/create/</b></code> <code>(creates new car)</code></summary>

Permissions: Admin or Security </br>
Statuses:
200 400 500


##### Parameters

| name         | type     | data type | description                      |
|--------------|----------|-----------|----------------------------------|
| `car_number` | required | string    | Car number in correct format     |
| `car_type`   | required | string    | Car type - See look-up tables    |
| `car_mark`   | required | string    | Car mark - See look-up tables    |
| `owner`      | optional | string    | Car id that needs to be returned |


##### Response
| name      | data type | description                                                                             |
|-----------|-----------|-----------------------------------------------------------------------------------------|
| `result`  | id        | id of created car                                                                       |

</details>

## Car marks
<details>
 <summary><code>GET</code> <code><b>/api/cars/marks/get-all/</b></code> <code>(returns all car marks and their ids)</code></summary>

Permissions: Admin or Security </br>
Statuses:
200

##### Parameters
 No

##### Response
| name      | data type     | description                                                                             |
|-----------|---------------|-----------------------------------------------------------------------------------------|
| `result`  | List[CarMark] | List of car marks with ids                                                              |

</details>

## Car types
<details>
 <summary><code>GET</code> <code><b>/api/cars/types/get-all/</b></code> <code>(returns all car types and their ids)</code></summary>

Permissions: Admin or Security </br>
Statuses:
200

##### Parameters

No 

##### Response
| name      | data type     | description                |
|-----------|---------------|----------------------------|
| `result`  | List[CarType] | List of car types with ids |

</details>

---

# Entrance request

<details>
 <summary><code>GET</code> <code><b>api/entrance-request/get all</b></code> <code>(returns all current entrance requests)</code></summary>

Returns all entrance requests. 
By default, only active withing 24 hours.

Permissions: Authenticated </br>
Statuses:
200

##### Parameters

| name           | type     | data type | description                         |
|----------------|----------|-----------|-------------------------------------|
| `period_start` | optional | string    | First date when requests are needed |
| `period_end`   | optional | string    | Last date when requests are needed  |

##### Response
| name      | data type             | description                                                                             |
|-----------|-----------------------|-----------------------------------------------------------------------------------------|
| `result`  | List[EntranceRequest] | list of all current entrance request                                                    |

</details>

<details>
 <summary><code>GET</code> <code><b>api/entrance-request/get-by-id</b></code> <code>(returns request by id)</code></summary>

Returns entrance requests by id.

Permissions: Authenticated</br>
Statuses:
200 400 404

##### Parameters

| name         | type     | data type | description       |
|--------------|----------|-----------|-------------------|
| `id`         | required | int       | id of GateRequest |

##### Response
| name      | data type        | description                                                                             |
|-----------|------------------|-----------------------------------------------------------------------------------------|
| `result`  | EntranceRequest  | Entrance request                                                                        |

</details>

<details>
 <summary><code>POST</code> <code><b>api/entrance-request/create</b></code> <code>(creates new entrance request)</code></summary>

Create new entrance request.

Permissions: Admin or Security </br>
Statuses:
200 400 500

##### Parameters

| name              | type     | data type | description                       |
|-------------------|----------|-----------|-----------------------------------|
| `request_account` | required | int       | Name of Personal account          |
| `car`             | required | int       | Id of requested car               |
| `is_car`          | required | bool      | is car or not - for adding humans |
| `is_paid`         | optional | bool      | Was the order paid                |
| `note`            | optional | string    | Any notes regarding request       |

##### Response
| name      | data type        | description                                                                                         |
|-----------|------------------|-----------------------------------------------------------------------------------------------------|
| `result`  | Entrance Request | id of created request    Created entrance request Indicates if the operation was successful or not. |

</details>

<details>
 <summary><code>DELETE</code> <code><b>api/entrance-request/delete-by-id</b></code> <code>(creates new entrance request)</code></summary>

Deletes entrance request.

Permissions: Admin or Security </br>
Statuses:
200 400 404


##### Parameters

| name | type     | data type | description                 |
|------|----------|-----------|-----------------------------|
| `id` | required | int       | Id of request to be deleted |

##### Response
| name      | data type        | description                                                                                         |
|-----------|------------------|-----------------------------------------------------------------------------------------------------|
| `result`  | Entrance Request | id of created request    Created entrance request Indicates if the operation was successful or not. |

</details>



___

# Address

## Personal Account
<details>
 <summary><code>GET</code> <code><b>/api/address/personal-account/get-all/</b></code> <code>(returns all personal accounts)</code></summary>

Permissions: Admin or Security </br>
Statuses:
200

##### Parameters

No 

##### Response
| name      | data type             | description |
|-----------|-----------------------|-------------|
| `result`  | List[PersonalAccount] | List of PA  |

</details>

## Streets - Not implemented
<details>
 <summary><code>GET</code> <code><b>/api/address/street/get-all/</b></code> <code>(returns all street names and their ids)</code></summary>

Permissions: Admin or Security </br>
Statuses:
200

##### Parameters

No 

##### Response
| name      | data type    | description              |
|-----------|--------------|--------------------------|
| `result`  | List[Street] | List of streets with ids |

</details>


## Addresses - Not implemented
<details>
 <summary><code>GET</code> <code><b>/api/address/address/get-all/</b></code> <code>(returns all addresses and their ids)</code></summary>

Permissions: Admin or Security </br>
Statuses:
200 400

##### Parameters

No 

##### Response
| name      | data type     | description              |
|-----------|---------------|--------------------------|
| `result`  | List[Address] | List of streets with ids |

</details>