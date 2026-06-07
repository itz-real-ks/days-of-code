# Schema Validator Part 6

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

```text
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}
```

## Notes

- The pipe (`|`) symbol means **"or"**. `role` must be one of the listed `Roles` values.
- The question mark (`?`) after `supporter` means that the field is **optional**, but must be of the specified type if it exists.
- `UserProfile[]` denotes an array of `UserProfile` objects. An empty array is valid.
- Extra keys are allowed.

