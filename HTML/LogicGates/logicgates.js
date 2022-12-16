function submit() {
  let gate = document.getElementById("gate").value;
  let input1 = document.getElementById("input1").value;
  let input2 = document.getElementById("input2").value;
  let output = document.getElementById("output");
  if (gate === "AND") {
    if (input1 === "1" && input2 === "1") {
      output.innerHTML = "Output: 1";
    } else {
      output.innerHTML = "Output: 0";
    }
  } else if (gate === "OR") {
    if (input1 === "1" || input2 === "1") {
      output.innerHTML = "Output: 1";
    } else {
      output.innerHTML = "Output: 0";
    }
  } else if (gate === "XOR") {
    if (
      (input1 === "1" && input2 === "0") ||
      (input1 === "0" && input2 === "1")
    ) {
      output.innerHTML = "Output: 1";
    } else {
      output.innerHTML = "Output: 0";
    }
  } else if (gate === "NOT") {
    if (input1 === "1" || input2 === "1") {
      output.innerHTML = "Output: 0";
    } else {
      output.innerHTML = "Output: 1";
    }
  } else if (gate === "NAND") {
    if (input1 === "1" && input2 === "1") {
      output.innerHTML = "Output: 0";
    } else {
      output.innerHTML = "Output: 1";
    }
  } else if (gate === "NOR") {
    if (input1 === "1" || input2 === "1") {
      output.innerHTML = "Output: 0";
    } else {
      output.innerHTML = "Output: 1";
    }
  } else if (gate === "XNOR") {
    if (
      (input1 === "1" && input2 === "0") ||
      (input1 === "0" && input2 === "1")
    ) {
      output.innerHTML = "Output: 0";
    } else {
      output.innerHTML = "Output: 1";
    }
    // add DNA logic gates
  } else if (gate === "DNA AND") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "T") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "A") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "T") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "DNA OR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "T") {
      output.innerHTML = "Output: A";
    } else if (input1 === "T" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "T" && input2 === "T") {
      output.innerHTML = "Output: T";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "DNA XOR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "T") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "A") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "T") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "DNA NOT") {
    if (input1 === "A") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "DNA NAND") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: T";
    } else if (input1 === "A" && input2 === "T") {
      output.innerHTML = "Output: A";
    } else if (input1 === "T" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "T" && input2 === "T") {
      output.innerHTML = "Output: T";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "DNA NOR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: T";
    } else if (input1 === "A" && input2 === "T") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "A") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "T") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "DNA XNOR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "T") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "A") {
      output.innerHTML = "Output: T";
    } else if (input1 === "T" && input2 === "T") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
    // add RNA logic gates
  } else if (gate === "RNA AND") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "U") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "U") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "RNA OR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "U") {
      output.innerHTML = "Output: A";
    } else if (input1 === "U" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "U" && input2 === "U") {
      output.innerHTML = "Output: U";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "RNA XOR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "U") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "U") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "RNA NOT") {
    if (input1 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "RNA NAND") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "A" && input2 === "U") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "U") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "RNA NOR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "A" && input2 === "U") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "U") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else if (gate === "RNA XNOR") {
    if (input1 === "A" && input2 === "A") {
      output.innerHTML = "Output: A";
    } else if (input1 === "A" && input2 === "U") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "A") {
      output.innerHTML = "Output: U";
    } else if (input1 === "U" && input2 === "U") {
      output.innerHTML = "Output: A";
    } else {
      output.innerHTML = "Invalid input";
    }
  } else {
    output.innerHTML = "Invalid input";
  }
  // when submit button is clicked again, the output is cleared
  document.getElementById("gate").value = "AND";
  document.getElementById("input1").value = "";
  document.getElementById("input2").value = "";
}

function mode() {
  document.getElementById("DNA").style.display = "block";
  document.getElementById("RNA").style.display = "block";
  var gate = document.getElementById("gate");
  var option = document.createElement("option");
  option.text = "DNA AND";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "DNA OR";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "DNA XOR";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "DNA NOT";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "DNA NAND";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "DNA NOR";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "DNA XNOR";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "RNA AND";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "RNA OR";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "RNA XOR";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "RNA NOT";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "RNA NAND";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "RNA NOR";
  gate.add(option);
  var option = document.createElement("option");
  option.text = "RNA XNOR";
  gate.add(option);
  // change the button's onclick function to modeReset()
  document.getElementById("mode").setAttribute("onclick", "modeReset()");
}
function modeReset() {
  document.getElementById("DNA").style.display = "none";
  document.getElementById("RNA").style.display = "none";
  var gate = document.getElementById("gate");
  // remove specific options from the dropdown menu
  // remove last 14 options
  for (var i = 8; i < 22; i++) {
    gate.remove(gate.length - 1);
  }
  document.getElementById("output").innerHTML = "";
  document.getElementById("mode").setAttribute("onclick", "mode()");
}
