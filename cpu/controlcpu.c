#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <tlhelp32.h>

void list_processes(const char *filename) {
    HANDLE hProcessSnap;
    PROCESSENTRY32 pe32;
    FILE *file = fopen(filename, "w");

    if (!file) {
        perror("Failed to open file");
        return;
    }

    // Lấy một snapshot của tất cả các tiến trình
    hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hProcessSnap == INVALID_HANDLE_VALUE) {
        fprintf(file, "Failed to create process snapshot.\n");
        fclose(file);
        return;
    }

    pe32.dwSize = sizeof(PROCESSENTRY32);

    // Lấy thông tin tiến trình đầu tiên
    if (!Process32First(hProcessSnap, &pe32)) {
        fprintf(file, "Failed to retrieve process information.\n");
        CloseHandle(hProcessSnap);
        fclose(file);
        return;
    }

    // Lặp qua tất cả các tiến trình và ghi thông tin vào file
    do {
        fprintf(file, "PID: %lu, Name: %s\n", pe32.th32ProcessID, pe32.szExeFile);
    } while (Process32Next(hProcessSnap, &pe32));

    CloseHandle(hProcessSnap);
    fclose(file);
    printf("Process list exported to %s\n", filename);
}

void set_process_priority(DWORD pid) {
    HANDLE hProcess = OpenProcess(PROCESS_SET_INFORMATION, FALSE, pid);
    if (hProcess == NULL) {
        perror("OpenProcess");
        exit(EXIT_FAILURE);
    }

    if (!SetPriorityClass(hProcess, IDLE_PRIORITY_CLASS)) {
        perror("SetPriorityClass");
        CloseHandle(hProcess);
        exit(EXIT_FAILURE);
    }

    CloseHandle(hProcess);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <PID>\n", argv[0]);
        printf("Listing all processes and exporting to process_list.txt:\n");
        list_processes("process_list.txt");
        return EXIT_FAILURE;
    }

    DWORD pid = atoi(argv[1]);

    // Thiết lập mức độ ưu tiên cho tiến trình
    set_process_priority(pid);
    printf("Set process priority for PID %lu to IDLE_PRIORITY_CLASS.\n", pid);

    return EXIT_SUCCESS;
}
