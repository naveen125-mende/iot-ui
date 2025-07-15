function moveNext(current, nextId) {
    if (current.value.length === 1) {
        const next = document.getElementById(nextId);
        if (next) next.focus();
    }
}
function hideLastBox(input) {
    if (input.value.length === 1) {
        input.classList.add("hidden");
    }
}

function combineOtp() {
    const otp = [
        document.getElementById('otp1').value,
        document.getElementById('otp2').value,
        document.getElementById('otp3').value,
        document.getElementById('otp4').value,
        document.getElementById('otp5').value,
        document.getElementById('otp6').value
    ].join('');
    document.getElementById('combinedOtp').value = otp;
    return true;
}
