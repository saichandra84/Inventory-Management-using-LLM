# Inventory Service

This service manages a simple in-memory inventory of `tshirts` and `pants`.

## Endpoints

### GET /inventory
Returns current inventory.

### POST /inventory
Updates inventory count.

```json
{
  "item": "tshirts",
  "change": -3
}
