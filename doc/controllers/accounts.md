# Accounts

```python
accounts_controller = client.accounts
```

## Class Name

`AccountsController`


# Delete Locataire

```python
def delete_locataire(self,
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
body.email = 'agent1@nexcode.dz'

result = accounts_controller.delete_locataire(body)
```

