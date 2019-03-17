# Vue.js

## Creating a new project with the Vue CLI

Perhaps, the easiest way is to just install the vue-cli:

```bash
yarn global add @vue/cli
# or
npm install -g @vue/cli
```

and then create your project template right away:[^vue-create]

```bash
vue create hello-world
```

!!! warning
    You might find a lot of tutorials online using the `vue init webpack project_name` command instead. As far as the documentation is concerned, this is already a legacy (Vue CLI 2) approach, and I would not recommend using it for new projects. Instead, stick to the much easier Vue CLI >= 3 approach described above[^vue-init].

[^vue-create]: [Creating a Project | Vue.js Docs](https://cli.vuejs.org/guide/creating-a-project.html#vue-create)
[^vue-init]: [Pulling 2.x Templates (Legacy) | Vue.js Docs](https://cli.vuejs.org/guide/creating-a-project.html#pulling-2-x-templates-legacy)

## Working with TypeScript

When working with TypeScript, make sure that your components also extend from `Vue`. Othewise, you can get a pretty nasty message by the TS compiler that `this.$store` or anything else that you might expect to be accessible inside your Vue component, is actually `undefined`.

So insted of this (vanilla JS):

```html
<script>
  export default {
    // code goes here...
  };
</script>
```

use this (TypeScript):

```typescript
<script lang="ts">
  import Vue from 'vue' export default Vue.extend(
  {
    // code goes here
  })
</script>
```
