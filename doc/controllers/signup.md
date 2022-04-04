# Signup

```python
signup_controller = client.signup
```

## Class Name

`SignupController`

## Methods

* [Signup New Locataire](../../doc/controllers/signup.md#signup-new-locataire)
* [Sign up Agent](../../doc/controllers/signup.md#sign-up-agent)
* [Validate Locataire](../../doc/controllers/signup.md#validate-locataire)
* [Reject Locataire](../../doc/controllers/signup.md#reject-locataire)
* [Admin](../../doc/controllers/signup.md#admin)
* [Decideur](../../doc/controllers/signup.md#decideur)


# Signup New Locataire

```python
def signup_new_locataire(self,
                        name,
                        family_name,
                        email,
                        phone_number,
                        password,
                        personal_photo,
                        photo_identity)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Form, Required | - |
| `family_name` | `string` | Form, Required | - |
| `email` | `string` | Form, Required | - |
| `phone_number` | `int` | Form, Required | - |
| `password` | `string` | Form, Required | - |
| `personal_photo` | `string` | Form, Required | - |
| `photo_identity` | `string` | Form, Required | - |

## Response Type

`void`

## Example Usage

```python
name = 'mohamed'
family_name = 'gouaouri'
email = 'im_gouaouri@esi.dz'
phone_number = 133993627
password = 'password'
personal_photo = 'personal_photo8'
photo_identity = 'photo_identity0'

result = signup_controller.signup_new_locataire(name, family_name, email, phone_number, password, personal_photo, photo_identity)
```


# Sign up Agent

```python
def sign_up_agent(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SignUpAgentRequest`](../../doc/models/sign-up-agent-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = SignUpAgentRequest()
body.name = 'agent1'
body.family_name = 'agent2'
body.email = 'agent1@nexcode.dz'
body.phone_number = '077766556665'
body.password = 'password'

result = signup_controller.sign_up_agent(body)
```


# Validate Locataire

```python
def validate_locataire(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteLocataireRequest`](../../doc/models/delete-locataire-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = DeleteLocataireRequest()
body.email = 'im_gouaouri@esi.dz'

result = signup_controller.validate_locataire(body)
```


# Reject Locataire

```python
def reject_locataire(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RejectLocataireRequest`](../../doc/models/reject-locataire-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = RejectLocataireRequest()
body.email = 'im_gouaouri@esi.dz'
body.justificatif = 'Une justification par l admin'

result = signup_controller.reject_locataire(body)
```


# Admin

```python
def admin(self,
         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Adminrequest`](../../doc/models/adminrequest.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = Adminrequest()
body.name = 'admin'
body.family_name = 'admin'
body.email = 'admin@nexcode.dz'
body.password = 'password'

result = signup_controller.admin(body)
```


# Decideur

```python
def decideur(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SignUpAgentRequest`](../../doc/models/sign-up-agent-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = SignUpAgentRequest()
body.name = 'decideur2'
body.family_name = 'decideur1'
body.email = 'decideur1@nexcode.dz'
body.phone_number = '077766556665'
body.password = 'password'

result = signup_controller.decideur(body)
```

