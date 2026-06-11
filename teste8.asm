section .data
  format_out: db "%d", 10, 0 ; format do printf
  format_in: db "%d", 0 ; format do scanf
  scan_int: dd 0; 32-bits integer

section .text
  extern printf ; usar _printf para Windows
  extern scanf ; usar _scanf para Windows
  ; extern _ExitProcess@4 ; usar para Windows
  global _start ; inicio do programa

_start:
  push ebp ; guarda o EBP
  mov ebp, esp ; zera a pilha

  ; aqui comeca o codigo gerado:

  sub esp, 4 ; var x i32 [EBP-4]
  mov eax, 10
  mov [ebp-4], eax ; x =
  mov eax, [ebp-4] ; x
  push eax
  push format_out
  call printf
  add esp, 8

  ; aqui termina o codigo gerado

  mov esp, ebp ; reestabelece a pilha
  pop ebp

  ; chamada da interrupcao de saida (Linux)
  mov eax, 1
  xor ebx, ebx
  int 0x80
  ; Para Windows:
  ; push dword 0
  ; call _ExitProcess@4
