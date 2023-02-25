<template>
    <div v-html="src" class="svg"></div>
</template>
<script>
export default {
    props: {
        name: {
            type: String,
            default: () => "",
        },
    },
    data() {
        return {
            icon: null
        }
    },
    computed: {
        src() {
            const src = require(`assets/icons/${this.name}.svg?raw`)
            return src
        }
    },
}
</script>
<style lang="scss" scoped>
.svg {
    margin-bottom: 20px;
    width: 20px;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    
    :deep() svg {
        width: 100%;
        height: 100%;
        fill: red;
    }
}
</style>