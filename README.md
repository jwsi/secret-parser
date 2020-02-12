# Secret Parser Action

Replaces GitHub Actions secrets referenced in files with their raw values.

## Inputs

### `filename`

**Required** File where GitHub Actions Secrets references should be parsed and replaced.

### `secret-name`

**Required** Name of secret to search for in the designated file.

### `secret-value`

**Required** Value of secret to replace reference with in designated file.

## Example usage

1. Create a file in the repository which references GitHub actions secret. For example, `test.json`:

```
{
  "important_value" : "${{ secrets.important_value }}"
}
```

2. Create a GitHub action secret with a key of: `important_value`

3. Add the following to your workflow configuration file (parameters shown below are for this demonstration only):

```
uses: jwsi/secret-parser@v1
with:
  filename: test.json
  secret-name: important_value
  secret-value: ${{ secrets.important_value }}
```

4. During workflow execution, `test.json` (or a file of one's choosing) will be parsed and the reference to a GitHub secret will be replaced with the corresponding secret value.