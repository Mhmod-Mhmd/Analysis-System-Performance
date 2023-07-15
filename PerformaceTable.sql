USE [System_Information]
GO

/****** Object:  Table [dbo].[Performance]    Script Date: 7/15/2023 11:06:37 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Performance](
	[time] [datetime] NULL,
	[CPU_percent_usage] [numeric](5, 2) NULL,
	[Memory_percent_usage] [numeric](5, 2) NULL,
	[CPU_interrupts] [numeric](18, 0) NULL,
	[CPU_calls] [numeric](18, 0) NULL,
	[Memory_used] [numeric](18, 0) NULL,
	[Memory_free] [numeric](18, 0) NULL,
	[Bytes_send] [numeric](18, 0) NULL,
	[Bytes_received] [numeric](18, 0) NULL,
	[Disk_percent_usage] [numeric](5, 2) NULL,
	[Memory_total] [numeric](18, 0) NULL,
	[Memory_available] [numeric](18, 0) NULL,
	[Disk_total] [numeric](18, 0) NULL,
	[Disk_used] [numeric](18, 0) NULL,
	[Disk_free] [numeric](18, 0) NULL
) ON [PRIMARY]
GO


