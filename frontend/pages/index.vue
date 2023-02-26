<template>
  <blocks-map></blocks-map> <!-- :items="items" -->
</template>

<script>
export default {
  head() {
		return {
			title: `Sport Objects Map`,
			meta: [
				{
					hid: "description",
					name: "description",
					// content: this.article.description,
				},
				// { hid: 'og:site_name', property: 'og:site_name', content: `${this.$base.title}` }, //process.env.BASE_TITLE
				// { hid: 'og:title', property: 'og:title', content: `${this.$base.title}` },
				// { hid: 'og:description', property: 'og:description', content: this.article.description },
				// { hid: 'og:url', property: 'og:url', content: `${this.$base.url}` }, // process.env.BASE_URL
				// { hid: 'og:image', property: 'og:image', content: `${this.article.image}` }, // LOGO
			],
        }
    },
}
</script>


