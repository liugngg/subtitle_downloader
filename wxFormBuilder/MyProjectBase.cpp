///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "MyProjectBase.h"

///////////////////////////////////////////////////////////////////////////

mainFrame::mainFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_3DLIGHT ) );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );

	m_panel = new wxPanel( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	m_panel->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	wxBoxSizer* main_sizer;
	main_sizer = new wxBoxSizer( wxVERTICAL );

	wxStaticBoxSizer* sbSizer1;
	sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( m_panel, wxID_ANY, _("文件目录设置") ), wxVERTICAL );

	wxBoxSizer* h0_sizer;
	h0_sizer = new wxBoxSizer( wxHORIZONTAL );

	m_staticText4 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, _("片名:"), wxDefaultPosition, wxSize( 60,-1 ), 0 );
	m_staticText4->Wrap( -1 );
	h0_sizer->Add( m_staticText4, 0, wxALL, 5 );

	name_input = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_PROCESS_ENTER );
	h0_sizer->Add( name_input, 1, wxALL, 5 );

	reset_button = new wxButton( sbSizer1->GetStaticBox(), wxID_ANY, _("重置"), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	h0_sizer->Add( reset_button, 0, wxALL, 5 );

	rename_button = new wxButton( sbSizer1->GetStaticBox(), wxID_ANY, _("创建目录"), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	h0_sizer->Add( rename_button, 0, wxALL, 5 );


	sbSizer1->Add( h0_sizer, 0, wxALL|wxEXPAND, 5 );

	wxBoxSizer* h1_sizer;
	h1_sizer = new wxBoxSizer( wxHORIZONTAL );


	h1_sizer->Add( 0, 0, 1, wxEXPAND, 5 );

	is_av = new wxCheckBox( sbSizer1->GetStaticBox(), wxID_ANY, _("番号"), wxDefaultPosition, wxDefaultSize, 0 );
	is_av->SetValue(true);
	h1_sizer->Add( is_av, 0, wxALL, 5 );

	is_4k = new wxCheckBox( sbSizer1->GetStaticBox(), wxID_ANY, _("4K"), wxDefaultPosition, wxDefaultSize, 0 );
	h1_sizer->Add( is_4k, 0, wxALL, 5 );

	is_crack = new wxCheckBox( sbSizer1->GetStaticBox(), wxID_ANY, _("破解"), wxDefaultPosition, wxDefaultSize, 0 );
	is_crack->SetValue(true);
	h1_sizer->Add( is_crack, 0, wxALL, 5 );

	is_enhance = new wxCheckBox( sbSizer1->GetStaticBox(), wxID_ANY, _("增强"), wxDefaultPosition, wxDefaultSize, 0 );
	h1_sizer->Add( is_enhance, 0, wxALL, 5 );

	is_leaked = new wxCheckBox( sbSizer1->GetStaticBox(), wxID_ANY, _("流出"), wxDefaultPosition, wxDefaultSize, 0 );
	h1_sizer->Add( is_leaked, 0, wxALL, 5 );

	is_cn = new wxCheckBox( sbSizer1->GetStaticBox(), wxID_ANY, _("中字"), wxDefaultPosition, wxDefaultSize, 0 );
	is_cn->SetValue(true);
	h1_sizer->Add( is_cn, 0, wxALL, 5 );


	sbSizer1->Add( h1_sizer, 1, wxALL|wxEXPAND, 5 );

	wxBoxSizer* h3_sizer;
	h3_sizer = new wxBoxSizer( wxHORIZONTAL );

	m_staticText5 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, _("保存目录:"), wxDefaultPosition, wxSize( 55,-1 ), 0 );
	m_staticText5->Wrap( -1 );
	h3_sizer->Add( m_staticText5, 0, wxALL, 5 );

	dir_input = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_READONLY );
	dir_input->DragAcceptFiles( true );

	h3_sizer->Add( dir_input, 1, wxALL, 5 );

	browse_button = new wxButton( sbSizer1->GetStaticBox(), wxID_ANY, _("浏览..."), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	h3_sizer->Add( browse_button, 0, wxALL, 5 );

	open_dir_button = new wxButton( sbSizer1->GetStaticBox(), wxID_ANY, _("打开目录"), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	h3_sizer->Add( open_dir_button, 0, wxALL, 5 );


	sbSizer1->Add( h3_sizer, 1, wxALL|wxEXPAND, 5 );


	main_sizer->Add( sbSizer1, 0, wxALL|wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer2;
	sbSizer2 = new wxStaticBoxSizer( new wxStaticBox( m_panel, wxID_ANY, _("字幕查询下载") ), wxVERTICAL );

	wxBoxSizer* h4_sizer;
	h4_sizer = new wxBoxSizer( wxHORIZONTAL );

	m_staticText6 = new wxStaticText( sbSizer2->GetStaticBox(), wxID_ANY, _("批量下载数量："), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText6->Wrap( -1 );
	h4_sizer->Add( m_staticText6, 0, wxALL, 10 );

	batch_count_spin = new wxSpinCtrl( sbSizer2->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxSP_ARROW_KEYS, 1, 10, 5 );
	h4_sizer->Add( batch_count_spin, 0, wxALL, 5 );


	h4_sizer->Add( 0, 0, 1, wxEXPAND, 5 );

	batch_download_button = new wxButton( sbSizer2->GetStaticBox(), wxID_ANY, _("批量下载"), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	h4_sizer->Add( batch_download_button, 0, wxALL, 5 );

	download_selected_button = new wxButton( sbSizer2->GetStaticBox(), wxID_ANY, _("下载选中"), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	h4_sizer->Add( download_selected_button, 0, wxALL, 5 );

	search_button = new wxButton( sbSizer2->GetStaticBox(), wxID_ANY, _("查询字幕"), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	h4_sizer->Add( search_button, 0, wxALL, 5 );


	h4_sizer->Add( 5, 0, 0, wxEXPAND, 5 );


	sbSizer2->Add( h4_sizer, 0, wxEXPAND, 5 );

	wxBoxSizer* v_listCtrl;
	v_listCtrl = new wxBoxSizer( wxVERTICAL );

	result_list = new wxListCtrl( sbSizer2->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLC_HRULES|wxLC_REPORT|wxLC_VRULES );
	v_listCtrl->Add( result_list, 1, wxEXPAND, 0 );


	sbSizer2->Add( v_listCtrl, 1, wxEXPAND, 5 );


	main_sizer->Add( sbSizer2, 1, wxALL|wxEXPAND, 5 );


	m_panel->SetSizer( main_sizer );
	m_panel->Layout();
	main_sizer->Fit( m_panel );
	bSizer1->Add( m_panel, 1, wxEXPAND | wxALL, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();
	status_bar = this->CreateStatusBar( 2, wxSTB_SIZEGRIP, wxID_ANY );

	this->Centre( wxBOTH );

	// Connect Events
	name_input->Connect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( mainFrame::on_search ), NULL, this );
	reset_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( mainFrame::on_reset ), NULL, this );
	rename_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( mainFrame::on_create_dir ), NULL, this );
	browse_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( mainFrame::on_browse ), NULL, this );
	open_dir_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( mainFrame::on_open_dir ), NULL, this );
	batch_download_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( mainFrame::on_batch_download ), NULL, this );
	download_selected_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( mainFrame::on_download_selected ), NULL, this );
	search_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( mainFrame::on_search ), NULL, this );
	status_bar->Connect( wxEVT_LEFT_DCLICK, wxMouseEventHandler( mainFrame::on_top_window ), NULL, this );
}

mainFrame::~mainFrame()
{
}
