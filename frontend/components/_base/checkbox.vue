<template>
    <label class="wrapper flex items-center" v-bind:class="{active: isChecked}">
        <slot/>
        <input class="checkbox" type="checkbox" :checked="isChecked" :value="value" @change="updateInput" />
        <span class="checkmark"></span>
    </label>
</template>

<script>
export default {
    model: {
        prop: "modelValue",
        event: "change",
    },
    props: {
        value: { type: String },
        modelValue: { default: "" },
        //label: { type: String, required: true },
        trueValue: { default: true },
        falseValue: { default: false },
    },
    computed: {
        isChecked() {
            if (this.modelValue instanceof Array) {
                return this.modelValue.includes(this.value);
            }
            // Note that `true-value` and `false-value` are camelCase in the JS
            return this.modelValue === this.trueValue;
        },
    },
    methods: {
        updateInput(event) {
            let isChecked = event.target.checked;
            if (this.modelValue instanceof Array) {
                let newValue = [...this.modelValue];
                if (isChecked) {
                    newValue.push(this.value);
                } else {
                    newValue.splice(newValue.indexOf(this.value), 1);
                }
                this.$emit("change", newValue);
            } else {
                this.$emit(
                    "change",
                    isChecked ? this.trueValue : this.falseValue
                );
            }
        },
    },
};
</script>

<style lang="scss" scoped>
/* Customize the label (the wrapper) */
.wrapper {
    display: inline-flex;
    align-items: center;
    position: relative;
    flex-direction: row-reverse;
    margin-bottom: 0px;
    cursor: pointer;
    user-select: none;
    color: $color-1;
    p {
        color: $color-7;
        font-weight: normal;
        font-size: 14px;
        line-height: 14px;
        padding-left: 8px;
        // margin-top: 3px;
    }
}
/* Hide the browser's default checkbox */
.wrapper input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
}
/* Create a custom checkbox */
.checkmark {
    position: relative;
    height: 14px;
    width: 14px;
    border-radius: 2px;
    background-color: transparent;
    border: 1px solid #828282;
}
/* On mouse-over, add a grey background color */
.wrapper:hover input ~ .checkmark {
    background-color: #808080;
}
/* When the checkbox is checked, add a $color-3 background */
.wrapper input:checked ~ .checkmark {
    background-color: $color-3;
    border-color: $color-3;
}
/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
    content: "";
    position: absolute;
    display: none;
}
/* Show the checkmark when checked */

/* Style the checkmark/indicator */
.wrapper .checkmark:after {
    left: 4px;
    top: 0px;
    width: 5px;
    height: 9px;
    border: solid $color-3;
    border-width: 0 2px 2px 0;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
}
.wrapper input:checked ~ .checkmark:after {
    display: block;
    border-color: #fff;
}
</style>