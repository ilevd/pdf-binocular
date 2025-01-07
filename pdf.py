from pypdf import PdfReader, PdfWriter, Transformation


def generate_pdf(file_name, postfix="_binocular", crop_v=0, crop_h=0, gap=0):
    print(f'Generating pdf for: {file_name}')

    with PdfReader(file_name) as reader, PdfWriter() as writer:
        pages_num = len(reader.pages)
        mbox = reader.pages[0].mediabox
        page_width, page_height = mbox.width, mbox.height

        def run():
            for ind in range(pages_num):
                writer.add_blank_page(page_width * 2 - crop_h * 2 - gap * 2,
                                      page_height - crop_v * 2)
                print(f"Page {ind + 1} / {pages_num}")
                page = reader.pages[ind]
                # left page
                page.cropbox.lower_left = (crop_h, crop_v)
                page.cropbox.upper_right = (page_width - crop_h - gap, page_height - crop_v)
                writer.pages[ind].merge_transformed_page(
                    page,
                    Transformation().translate(-crop_h, -crop_v))
                # right page
                page.cropbox.lower_left = (crop_h + gap, crop_v)
                page.cropbox.upper_right = (page_width - crop_h, page_height - crop_v)
                writer.pages[ind].merge_transformed_page(
                    page,
                    Transformation().translate(page_width - crop_h - gap * 2, -crop_v))

        run()
        print("Writing...")
        out_name = file_name.split('.')[0] + postfix + "." + file_name.split('.')[1]
        writer.write(out_name)
        print("Done")


generate_pdf('file.pdf', postfix=" binocular", crop_v=0, crop_h=0, gap=0)
