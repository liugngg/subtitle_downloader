///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/intl.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/sizer.h>
#include <wx/checkbox.h>
#include <wx/statbox.h>
#include <wx/spinctrl.h>
#include <wx/listctrl.h>
#include <wx/panel.h>
#include <wx/statusbr.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
/// Class mainFrame
///////////////////////////////////////////////////////////////////////////////
class mainFrame : public wxFrame
{
	private:

	protected:
		wxPanel* m_panel;
		wxStaticText* m_staticText4;
		wxTextCtrl* name_input;
		wxButton* reset_button;
		wxButton* rename_button;
		wxCheckBox* is_av;
		wxCheckBox* is_4k;
		wxCheckBox* is_crack;
		wxCheckBox* is_enhance;
		wxCheckBox* is_leaked;
		wxCheckBox* is_cn;
		wxStaticText* m_staticText5;
		wxTextCtrl* dir_input;
		wxButton* browse_button;
		wxButton* open_dir_button;
		wxStaticText* m_staticText6;
		wxSpinCtrl* batch_count_spin;
		wxButton* batch_download_button;
		wxButton* download_selected_button;
		wxButton* search_button;
		wxListCtrl* result_list;
		wxStatusBar* status_bar;

		// Virtual event handlers, override them in your derived class
		virtual void on_search( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_reset( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_create_dir( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_browse( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_open_dir( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_batch_download( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_download_selected( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_top_window( wxMouseEvent& event ) { event.Skip(); }


	public:

		mainFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = _("字幕查询下载工具-liugngg"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 748,561 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~mainFrame();

};

