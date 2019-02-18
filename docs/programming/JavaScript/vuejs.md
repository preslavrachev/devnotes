# Vue.js

## Working with TypeScript
When working with TypeScript, make sure that your components also extend from `Vue`. Othewise, you can get a pretty nasty message by the TS compiler that `this.$store` or anything else that you might expect to be accessible inside your Vue component, is actually `undefined`.

So insted of this (vanilla JS):

``` html
<script>
export default {
    // code goes here...
}
</script>
```

use this (TypeScript):

``` typescript
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    // code goes here
})
</script>
```
