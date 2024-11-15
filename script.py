# Copyright (C) Back Engineering Labs, Inc. - All Rights Reserved

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

for root, dirs, files in os.walk('.'):
    if {'func-leaf.csv', 'inst-data.csv', 'func-info.csv'}.issubset(files):
        func_leaf_path = os.path.join(root, 'func-leaf.csv')
        inst_data_path = os.path.join(root, 'inst-data.csv')
        func_info_path = os.path.join(root, 'func-info.csv')

        functions_df = pd.read_csv(func_leaf_path)
        instructions_df = pd.read_csv(inst_data_path)
        func_info_df = pd.read_csv(func_info_path)

        try:
            fig, axes = plt.subplots(5, 2, figsize=(14, 32))
            fig.suptitle(f"Binary Function and Instruction Analysis for \"{os.path.basename(root)}\"", fontsize=16)
            fig.subplots_adjust(top=0.93, hspace=0.4, wspace=0.3)

            # Top 10 Most Common Mnemonics
            top_10_mnemonics = instructions_df.groupby('Mnemonic')['Count'].sum().nlargest(10)
            sns.barplot(x=top_10_mnemonics.index, y=top_10_mnemonics.values, ax=axes[0, 0], palette="Blues_d")
            axes[0, 0].set_title("Top 10 Most Common Mnemonics")
            axes[0, 0].set_xlabel("Mnemonic")
            axes[0, 0].set_ylabel("Count")
            axes[0, 0].tick_params(axis='x', rotation=45, labelsize=10)
            axes[0, 0].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[0, 0].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # New Plot: Top 10 Largest Instructions by Length with Address Annotations
            largest_instructions = instructions_df.nlargest(11, 'Length')
            ax = sns.barplot(x=largest_instructions['Mnemonic'], y=largest_instructions['Length'], ax=axes[0, 1], palette="Blues_d")
            axes[0, 1].set_title("Top 10 Largest Instructions by Length")
            axes[0, 1].set_xlabel("")
            axes[0, 1].set_ylabel("Instruction Length (Bytes)")
            axes[0, 1].tick_params(axis='x', rotation=45)
            axes[0, 1].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[0, 0].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # Instruction Length Distribution
            length_counts = instructions_df['Length'].value_counts().sort_index()
            sns.barplot(x=length_counts.index, y=length_counts.values, ax=axes[1, 0], palette="Blues_d")
            axes[1, 0].set_title("Distribution of Instruction Lengths in Bytes")
            axes[1, 0].set_xlabel("Instruction Byte Length")
            axes[1, 0].set_ylabel("Unique Instructions")
            axes[1, 0].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[1, 0].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # Memory Access Patterns
            memory_access_counts = instructions_df[['MemRead', 'MemWrite', 'CondMemRead', 'CondMemWrite']].sum()
            sns.barplot(x=memory_access_counts.index, y=memory_access_counts.values, ax=axes[1, 1], palette="Blues_d")
            axes[1, 1].set_title("Memory Access Patterns in Instructions")
            axes[1, 1].set_xlabel("Memory Access Type")
            axes[1, 1].set_ylabel("Unique Instructions")
            axes[1, 1].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[1, 1].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # Terminator Type Frequencies
            func_info_df['TerminatorType'] = func_info_df['Terminator'].apply(lambda x: x.split('(')[0])
            terminator_counts = func_info_df['TerminatorType'].value_counts()
            sns.barplot(x=terminator_counts.index, y=terminator_counts.values, ax=axes[2, 0], palette="Blues_d")
            axes[2, 0].set_title("Control Flow Frequencies")
            axes[2, 0].set_xlabel("")
            axes[2, 0].set_ylabel("Count")
            axes[2, 0].tick_params(axis='x', rotation=45)
            axes[2, 0].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[2, 0].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # Function Sizes
            function_sizes = func_info_df.groupby('Function')['Size'].sum()
            top_10_functions = function_sizes.nlargest(10)
            top_10_functions.index = ['sub_' + str(x) for x in top_10_functions.index]  # Add "sub_" prefix
            sns.barplot(x=top_10_functions.index, y=top_10_functions.values, ax=axes[2, 1], palette="Blues_d")
            axes[2, 1].set_title("Top 10 Largest Functions by Size")
            axes[2, 1].set_xlabel("Function Address")
            axes[2, 1].set_ylabel("Total Size (Bytes)")
            axes[2, 1].tick_params(axis='x', rotation=45)
            axes[2, 1].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[2, 1].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # Function Type Distribution
            function_type_counts = functions_df[['Leaf', 'FrameFunction', 'UnalignedFrameFunction']].sum()
            sns.barplot(x=function_type_counts.index, y=function_type_counts.values, ax=axes[3, 0], palette="Blues_d")
            axes[3, 0].set_title("Distribution of Function Types")
            axes[3, 0].set_xlabel("")
            axes[3, 0].set_ylabel("Count")
            axes[3, 0].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[3, 0].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # Top 15 Most Referenced Basic Blocks
            reference_counts = func_info_df.groupby('BasicBlock')['ReferenceCount'].sum()
            top_10_referenced_bbs = reference_counts.nlargest(15)
            sns.barplot(x=top_10_referenced_bbs.index, y=top_10_referenced_bbs.values, ax=axes[3, 1], palette="Blues_d")
            axes[3, 1].set_title("Top 15 Most Referenced Basic Blocks")
            axes[3, 1].set_xlabel("Function Address")
            axes[3, 1].set_ylabel("Total Reference Count")
            axes[3, 1].tick_params(axis='x', rotation=45)
            axes[3, 1].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[3, 1].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            # Basic Block Size Distribution
            sns.histplot(data=func_info_df, x='Size', ax=axes[4, 0], log_scale=(True, False), bins=30, palette="Blues_d")
            axes[4, 0].set_title("Basic Block Size Distribution (Log Scale)")
            axes[4, 0].set_xlabel("Basic Block Size (Bytes, Log Scale)")
            axes[4, 0].set_ylabel("Frequency")
            axes[4, 0].text(0.5, 0.5, 'Back Engineering Labs', transform=axes[4, 0].transAxes, fontsize=30, color='gray', alpha=0.5, ha='center', va='center', rotation=30)

            jcc_instructions = ['Ja', 'Jae', 'Jb', 'Jbe', 'Jcxz', 'Jecxz', 'Jg', 'Jge', 
                                'Jl', 'Jle', 'Jmp', 'Jmpe', 'Jne', 'Jno', 'Jnp', 'Jns', 
                                'Jo', 'Jp', 'Jrcxz', 'Js', 'Je', 'Jne']
            data_movements = ['Mov', 'Call', 'Movsx', 'Movzx']
            filtered_df = instructions_df[instructions_df['Mnemonic'].isin(data_movements + jcc_instructions)]
            filtered_df['Category'] = filtered_df['Mnemonic'].apply(
                lambda x: 'Control Flow and Data Movements' if x in (jcc_instructions + data_movements) else 'Other'
            )

            category_counts = filtered_df.groupby('Category')['Count'].sum()
            total_count = instructions_df['Count'].sum()
            others_count = total_count - category_counts.sum()
            category_counts['Other Instructions'] = others_count
            category_percentages = (category_counts / total_count) * 100
            category_percentages = category_percentages.reset_index()
            category_percentages.columns = ['Category', 'Percentage']

            sns.barplot(
                data=category_percentages,
                x='Category',
                y='Percentage',
                ax=axes[4, 1],
                palette="Blues_d"
            )
            axes[4, 1].set_title("Instruction Category Distribution")
            axes[4, 1].set_xlabel("Category")
            axes[4, 1].set_ylabel("Percentage (%)")
            axes[4, 1].tick_params(axis='x', rotation=15, labelsize=10)

            output_path = os.path.join(root, "results.png")
            plt.savefig(output_path, dpi=300)
            print(f"Saved analysis plot to: {output_path}")

        except Exception as e:
            print(f"Error processing directory {root}: {e}")
