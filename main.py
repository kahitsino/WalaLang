import os
import time
from cryptography.fernet import Fernet


os.chdir("folder") # PATH folder name
current_dir = os.getcwd()

key_path = "../secret/secret_key.key"
os.makedirs(os.path.dirname(key_path), exist_ok=True)

print("🔑 INITIALIZING ENCRYPTION SYSTEM")
print("=" * 40)

if os.path.exists(key_path):
    while True:
        use_existing_key = input("📁 Existing encryption key found\nUse existing key? (y/n): ").lower().strip()

        if use_existing_key == "y":
            try:
                with open(key_path, "rb") as key_file:
                    key = key_file.read()
                f = Fernet(key)
                print("⏳ Checking...")
                time.sleep(2)
                print("⏳ Loading existing key...")
                time.sleep(1)
                print("✅ Encryption key loaded successfully")
                break
            except Exception as e:
                print("⏳ Checking...")
                time.sleep(1)
                print("❌ Invalid key")
                time.sleep(1)
                print("🔄 Generating new key...")
                time.sleep(2)
                key = Fernet.generate_key()
                with open(key_path, "wb") as key_file:
                    key_file.write(key)
                f = Fernet(key)
                print("✅ New encryption key generated")
                break
        elif use_existing_key == "n":
            key = Fernet.generate_key()
            time.sleep(1)
            print("🔄 Generating new key...")
            with open(key_path, "wb") as key_file:
                key_file.write(key)
            f = Fernet(key)
            time.sleep(2)
            print("✅ New encrytion key generated")
            break
        else:
            print("⏳ Checking...")
            time.sleep(1)
            print("❌ Invalid choice please enter 'y' or 'n'")
    
else:
    print("🔄 Generating encryption key")
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    f = Fernet(key)
    print("✅ Encryption key generated")

print("=" * 40)

while True:
    choices_list = ["Encrypt", "Decrypt", "Inspect the Directories"]

    print("\n" + "=" * 50)
    print("ENCRYPTION MANAGER")
    print("=" * 50)

    for i, choice in enumerate(choices_list, 1):
        print(f"{i}. {choice}")
        
    print("=" * 50)
    choice = input("Select option (1-3): ")

    if choice == "1":
        current_explore_path = current_dir

        while True:
            all_items = os.listdir(current_explore_path)
            current_folders = []
            current_files = []

            for item in all_items:
                full_path = os.path.join(current_explore_path, item)
                if os.path.isdir(full_path):
                    current_folders.append(item)
                else:
                    current_files.append(item)

            print("\n" + "=" * 50)
            print(f"📁 CURRENT LOCATION: {os.path.basename(current_explore_path)}")
            print(f"📍 FULL PATH: {current_explore_path}")
            print("=" * 50)

            print("\n📂 FOLDERS")
            if current_folders:
                for i, folder in enumerate(current_folders, 1):
                    print(f"    [{i}] 📂 {folder}")
            else:
                print("    No Folder found")
            
            print("\n📄 FILES")
            if current_files:
                file_start_number = len(current_folders) + 1
                for i, file in enumerate(current_files, file_start_number):
                    file_path = os.path.join(current_explore_path, file)
                    file_size = os.path.getsize(file_path)
                    print(f"    [{i}] 📄 {file} ({file_size} bytes)")
            else:
                print("    No File found")

            total_items = len(current_folders) + len(current_files)

            is_root_folder = (current_explore_path == current_dir)
            is_inside_folder = not is_root_folder
    
            if is_inside_folder:
                back_option = total_items + 1
                encrypt_option = total_items + 2

                print("\n🔧 NAVIGATION OPTIONS:")
                print(f"    [{back_option}] ↩️ Back to previous folder")
                print(f"    [{encrypt_option}] 🔐 Encryption")
                max_option = encrypt_option
            else:
                back_main_option = total_items + 1
                encrypt_option = total_items + 2
                print(f"    [{back_main_option}] 🏠 Back to main menu")
                print(f"    [{encrypt_option}] 🔐 Encryption")
                max_option = encrypt_option

            user_choice = input(f"\n🎯 Enter your choice (1-{max_option}): ")

            if user_choice.isdigit():
                choice_num = int(user_choice)

                if 1 <= choice_num <= len(current_folders):
                    selected_folders = current_folders[choice_num-1]
                    current_explore_path = os.path.join(current_explore_path, selected_folders)

                    print(f"\n➡️ Entering folder: {selected_folders}")

                elif len(current_folders) < choice_num <= total_items:
                    selected_file_index = choice_num - len(current_folders) - 1

                    if selected_file_index >= 0 and selected_file_index < len(current_files):
                        selected_file = current_files[selected_file_index]
                        file_path = os.path.join(current_explore_path, selected_file)
                        print(f"\n🎯 Selected file: {selected_file}")
                        
                        try:
                            with open(file_path, "rb") as file:
                                file_data = file.read()

                            try:
                                f.decrypt(file_data)
                                time.sleep(1)
                                print("❌ This file is already encrypted!")
                                time.sleep(2)
                                print("💡 Please decrypt it first or select another file")
                                continue
                            except:
                                print("🔄 Encrypting file...")
                                time.sleep(1)
                                encrypted_data = f.encrypt(file_data)
                                with open(file_path, "wb") as file_encryption:
                                    file_encryption.write(encrypted_data)
                                
                                print("✅ File encrypted successfully!")
                                time.sleep(1)
                                print("⏸️ Returning to main menu...")
                                time.sleep(2)
                                break

                        except Exception as e:
                            print(f"❌ Encrytion failed: {e}")

                elif is_inside_folder and choice_num == back_option:
                    old_folder = os.path.basename(current_explore_path)
                    current_explore_path = os.path.dirname(current_explore_path)
                    new_folder = os.path.basename(current_explore_path)
                    print(f"↩️ Returning front {old_folder} to {new_folder}")

                elif not is_inside_folder and choice_num == back_main_option:
                    print("🏠 Returning to main menu...")
                    time.sleep(2)
                    break

                elif choice_num == encrypt_option:
                    print(f"\n🔐 ENCRYPTING FOLDER: {os.path.basename(current_explore_path)}")
                    print("⏳ This may take a moment...")
                    time.sleep(3)

                    encrypted_count = 0
                    skipped_count = 0

                    for root, dirs, files in os.walk(current_explore_path):
                        for file in files:
                            file_path = os.path.join(root, file)

                            try:
                                with open(file_path, "rb") as normal_folder:
                                    normal_folder_encrypted = normal_folder.read()
                            
                                try:
                                    f.decrypt(normal_folder_encrypted)
                                    time.sleep(1)
                                    print(f"⏭️ Skipped: {file} (already encrypted)")
                                    time.sleep(1)

                                    skipped_count += 1
                                    continue
                                
                                except:
                                    encrypted_data = f.encrypt(normal_folder_encrypted)
                                    with open(file_path, "wb") as encrypted_folder:
                                        encrypted_folder.write(encrypted_data)
                                    print(f"✅ Encrypted: {file}")
                                    encrypted_count += 1
                            except Exception as e:
                                print(f"❌ Failed: {file} - {e}")


                    print("\n📊 ENCRYPTION SUMMARY:")
                    print(f"    ✅ Successfully encrypted: {encrypted_count}")
                    print(f"    ⏭️ Skipped (already encrypted): {skipped_count}")
                    print(f"    📁 Folder: {os.path.basename(current_explore_path)}")
                    break

    elif choice == "2":
        current_explore_path = current_dir

        while True:
            all_items = os.listdir(current_explore_path)
            current_folders = []
            current_files = []

            for item in all_items:
                full_path = os.path.join(current_explore_path, item)
                if os.path.isdir(full_path):
                    current_folders.append(item)
                else:
                    current_files.append(item)

            print("\n" + "=" * 50)
            print(f"📁 CURRENT LOCATION: {os.path.basename(current_explore_path)}")
            print(f"📍 FULL PATH: {current_explore_path}")
            print("=" * 50)

            print("\n📂 FOLDERS")
            if current_folders:
                for i, folder in enumerate(current_folders, 1):
                    print(f"    [{i}] 📂 {folder}")
            else:
                print("    No Folder found")
            
            print("\n📄 FILES")
            if current_files:
                file_start_number = len(current_folders) + 1
                for i, file in enumerate(current_files, file_start_number):
                    file_path = os.path.join(current_explore_path, file)
                    file_size = os.path.getsize(file_path)
                    print(f"    [{i}] 📄 {file} ({file_size} bytes)")
            else:
                print("    No File found")

            total_items = len(current_folders) + len(current_files)

            is_root_folder = (current_explore_path == current_dir)
            is_inside_folder = not is_root_folder
    
            if is_inside_folder:
                back_option = total_items + 1
                decrypt_option = total_items + 2

                print("\n🔧 NAVIGATION OPTIONS:")
                print(f"    [{back_option}] ↩️ Back to previous folder")
                print(f"    [{decrypt_option}] 🔐 Decryption")
                max_option = decrypt_option
            else:
                back_main_option = total_items + 1
                decrypt_option = total_items + 2
                print(f"    [{back_main_option}] 🏠 Back to main menu")
                print(f"    [{decrypt_option}] 🔐 Decryption")
                max_option = decrypt_option

            user_choice = input(f"\n🎯 Enter your choice (1-{max_option}): ")

            if user_choice.isdigit():
                choice_num = int(user_choice)

                if 1 <= choice_num <= len(current_folders):
                    selected_folders = current_folders[choice_num-1]
                    current_explore_path = os.path.join(current_explore_path, selected_folders)

                    print(f"\n➡️ Entering folder: {selected_folders}")

                elif len(current_folders) < choice_num <= total_items:
                    selected_file_index = choice_num - len(current_folders) - 1

                    if selected_file_index >= 0 and selected_file_index < len(current_files):
                        selected_file = current_files[selected_file_index]
                        file_path = os.path.join(current_explore_path, selected_file)
                        print(f"\n🎯 Selected file: {selected_file}")
                        
                        try:
                            with open(file_path, "rb") as file:
                                file_data = file.read()

                            try:
                                print("🔄 Decrypting file...")
                                time.sleep(1)
                                decrypted_data = f.decrypt(file_data)
                                with open(file_path, "wb") as file_decryption:
                                    file_decryption.write(decrypted_data)
                                
                                print("✅ File decrypted successfully!")
                                time.sleep(1)
                                print("⏸️ Returning to main menu...")
                                time.sleep(2)
                                break

                                
                            except:
                                time.sleep(1)
                                print("❌ This file is not encrypted!")
                                time.sleep(2)
                                print("💡 File is in normal state")
                                continue

                        except Exception as e:
                            print(f"❌ Decrytion failed: {e}")

                elif is_inside_folder and choice_num == back_option:
                    old_folder = os.path.basename(current_explore_path)
                    current_explore_path = os.path.dirname(current_explore_path)
                    new_folder = os.path.basename(current_explore_path)
                    print(f"↩️ Returning front {old_folder} to {new_folder}")

                elif not is_inside_folder and choice_num == back_main_option:
                    print("🏠 Returning to main menu...")
                    time.sleep(2)
                    break

                elif choice_num == decrypt_option:
                    print(f"\n🔐 DECRYPTING FOLDER: {os.path.basename(current_explore_path)}")
                    print("⏳ This may take a moment...")
                    time.sleep(3)

                    decrypted_count = 0
                    skipped_count = 0

                    for root, dirs, files in os.walk(current_explore_path):
                        for file in files:
                            file_path = os.path.join(root, file)

                            try:
                                with open(file_path, "rb") as normal_folder:
                                    normal_folder_decrypted = normal_folder.read()
                            
                                try:
                                    decrypted_data = f.decrypt(normal_folder_decrypted)
                                    with open(file_path, "wb") as decrypted_folder:
                                        decrypted_folder.write(decrypted_data)
                                    print(f"✅ Decrypted: {file}")
                                    decrypted_count += 1
                                
                                except:
                                    time.sleep(1)
                                    print(f"⏭️ Skipped: {file} (file not encrypted)")
                                    time.sleep(1)

                                    skipped_count += 1
                                    continue
                            except Exception as e:
                                print(f"❌ Failed: {file} - {e}")


                    print("\n📊 DECRYPTION SUMMARY:")
                    print(f"    ✅ Successfully decrypted: {decrypted_count}")
                    print(f"    ⏭️ Skipped (already decrypted): {skipped_count}")
                    print(f"    📁 Folder: {os.path.basename(current_explore_path)}")
                    break

    elif choice == "3":
        print("\n" + "=" * 50)
        print("🔍 INSPECT FEATURE")
        print("=" * 50)
        print("🚧 UNDER CONSTRUCTION 🚧")
        print("\nThis feature is currently being developed.")
        print("It will allow you to view detailed file information")
        print("and check encryption status of files.")

        while True:
            time.sleep(3)
            print("\nReturning to main menu...")
            time.sleep(2)
            break