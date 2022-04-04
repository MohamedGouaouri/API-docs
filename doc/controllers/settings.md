# Settings

```python
settings_controller = client.settings
```

## Class Name

`SettingsController`

## Methods

* [Update Locataire Password](../../doc/controllers/settings.md#update-locataire-password)
* [Update Agent Password](../../doc/controllers/settings.md#update-agent-password)
* [Update Decideur Password](../../doc/controllers/settings.md#update-decideur-password)
* [Update Locataire Email](../../doc/controllers/settings.md#update-locataire-email)
* [Update Decideur Email](../../doc/controllers/settings.md#update-decideur-email)
* [Update Agent Email](../../doc/controllers/settings.md#update-agent-email)


# Update Locataire Password

```python
def update_locataire_password(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResetPasswordLocataireRequest`](../../doc/models/reset-password-locataire-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = ResetPasswordLocataireRequest()
body.password = 'passwordupdated'

result = settings_controller.update_locataire_password(body)
```


# Update Agent Password

```python
def update_agent_password(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResetPasswordLocataireRequest`](../../doc/models/reset-password-locataire-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = ResetPasswordLocataireRequest()
body.password = 'passwordupdated'

result = settings_controller.update_agent_password(body)
```


# Update Decideur Password

```python
def update_decideur_password(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResetPasswordLocataireRequest`](../../doc/models/reset-password-locataire-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = ResetPasswordLocataireRequest()
body.password = 'passwordupdated'

result = settings_controller.update_decideur_password(body)
```


# Update Locataire Email

```python
def update_locataire_email(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResetPasswordLocataireRequest`](../../doc/models/reset-password-locataire-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = ResetPasswordLocataireRequest()
body.password = 'passwordupdated'

result = settings_controller.update_locataire_email(body)
```


# Update Decideur Email

```python
def update_decideur_email(self,
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
body.email = 'dec@gmail.com'

result = settings_controller.update_decideur_email(body)
```


# Update Agent Email

```python
def update_agent_email(self,
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
body.email = 'agent@gmail.com'

result = settings_controller.update_agent_email(body)
```

