    .file    "chall.c"
    .text
    .section    .rodata
.LC0:
    .string    "Simple flag checker!, Input: "
.LC1:
    .string    "%s"
.LC2:
    .string    "Solved!"
    .text
    .globl    main
    .type    main, @function
main:
.LFB0:
    .cfi_startproc
    pushq    %rbp
    .cfi_def_cfa_offset 16
    .cfi_offset 6, -16
    movq    %rsp, %rbp
    .cfi_def_cfa_register 6
    subq    $320, %rsp
    leaq    .LC0(%rip), %rdi
    call    puts@PLT
    movabsq $8319050641287963497, %rax
    movabsq $8387496331138198835, %rdx
    movq    %rax, -48(%rbp)
    movq    %rdx, -40(%rbp)
    movabsq $7293129038958649207, %rax
    movl    $8217139, %edx
    movq    %rax, -32(%rbp)
    movq    %rdx, -24(%rbp)
    movb    $0, -16(%rbp)
    leaq    -320(%rbp), %rax
    movq    %rax, %rsi
    leaq    .LC1(%rip), %rdi
    movl    $0, %eax
    call    __isoc99_scanf@PLT
    leaq    -320(%rbp), %rdx
    leaq    -48(%rbp), %rax
    movq    %rdx, %rsi
    movq    %rax, %rdi
    call    strcmp@PLT
    testl    %eax, %eax
    jne    .L2
    leaq    .LC2(%rip), %rdi
    call    puts@PLT
.L2:
    movl    $0, %eax
    leave
    .cfi_def_cfa 7, 8
    ret
    .cfi_endproc
.LFE0:
    .size    main, .-main
    .ident    "GCC: (Debian 10.2.1-6) 10.2.1 20210110"
    .section    .note.GNU-stack,"",@progbits