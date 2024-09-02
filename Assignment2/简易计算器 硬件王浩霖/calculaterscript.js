function insert(num) {
    document.form.textview.value = document.form.textview.value + num;
}
function equal() {
    let exp = document.form.textview.value;
    if (exp) {
        try {
            let eval1 = eval(exp);
            if (typeof eval1 === 'number') {
                if (isFinite(eval1)) {
                    document.form.textview.value = eval1.toFixed(2);
                } else {
                    document.form.textview.value = "数字错误";
                }
            } else {
                document.form.textview.value = "语法错误";
            }
        } catch (e) {
            if (e instanceof SyntaxError) {
                document.form.textview.value = "语法错误";
            } else {
                document.form.textview.value = "错误";
            }
        }
    }
}
function Mclean() {
    document.form.textview.value = "";
}
function back(){
    let exp = document.form.textview.value;
    document.form.textview.value = exp.substring(0, exp.length - 1);
}