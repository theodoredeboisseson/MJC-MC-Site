module.exports = {
    content: [
        './apps/**/templates/**/*.html',
        './templates/**/*.html',
        './static/css/**/*.css',
    ],
    theme: {
        extend: {
            colors: {
                'brand-primary': '#2c3e50',
                'brand-secondary': '#2980b9',
                'brand-tertiary': '#e74c3c',
                'brand-quaternary': '#27ae60',
                'brand-quinary': '#f39c12',
                'brand-senary': '#8e44ad',
                'brand-septenary': '#16a085',
                'brand-octonary': '#d35400',
                'brand-nonary': '#c0392b',
                'brand-denary': '#7f8c8d',
                
                'primary': '#0013fa', /* # #5b9af5 D9381E #536B1E  #dcba4f */
                'secondary': '#CA552F', /* #297a62 #3A485B #81B29A */
                'background': '#f0f4f8', /* theme('colors.gray.100') */
                'dark-text': '#20223B', /* #222D06 theme('colors.gray.700') */
                'light-text': '#edf2f7', /* #FDFFE0 #E1D5BB */
                'link-hover': '#63b3ed', /* #F2CC8F */
                'primary-light': 'color-mix(in srgb, var(primary) 80%, white 10%)',
                'section-bg': '#efe7d3', /* #F4F1DE #D7D1C5 */
            },
        },
    },
    plugins: [],
};
